from textwrap import dedent

def water(last_atom_ID, last_bond_ID, last_angle_ID, model='TIP4P_cutoff'):

    ID_O = last_atom_ID + 1
    ID_H = ID_O + 1

    BT = last_bond_ID + 1
    AT = last_angle_ID + 1

    charge_dict = {
    'TIP4P_cutoff':      (-1.0400, 0.5200),
    'TIP4P_2005_cutoff': (-1.1128, 0.5564),
    'TIP4P_2005_long':   (-1.0484, 0.5242),
    'TIP3P_long':        (-0.8300, 0.4150)
    }

    M_site_dist_dict = {
    'TIP4P_cutoff':      0.1500,
    'TIP4P_2005_cutoff': 0.1546,
    'TIP4P_2005_long':   0.1250,
    'TIP3P_long':        None
    }

    LJ_dict = {
    # LAMMPS has a special TIP4P pair_style that automatically adds the M site
    'TIP4P_cutoff':      {ID_O: ('lj/cut/tip4p/cut' , 0.15500, 3.15360), ID_H: ('lj/cut/tip4p/cut' , 0.0, 0.0), 'style': 'lj/cut/tip4p/cut' , 'comments': {ID_O:['O_water', 'O_water'], ID_H:['H_water', 'H_water']}},
    'TIP4P_2005_cutoff': {ID_O: ('lj/cut/tip4p/long', 0.18520, 3.15890), ID_H: ('lj/cut/tip4p/long', 0.0, 0.0), 'style': 'lj/cut/tip4p/long', 'comments': {ID_O:['O_water', 'O_water'], ID_H:['H_water', 'H_water']}},
    'TIP4P_2005_long':   {ID_O: ('lj/cut/tip4p/long', 0.16275, 3.16435), ID_H: ('lj/cut/tip4p/long', 0.0, 0.0), 'style': 'lj/cut/tip4p/long', 'comments': {ID_O:['O_water', 'O_water'], ID_H:['H_water', 'H_water']}},
    'TIP3P_long':        {ID_O: ('lj/cut/coul/long' , 0.10200, 3.18800), ID_H: ('lj/cut/coul/long' , 0.0, 0.0), 'style': 'lj/cut/coul/long' , 'comments': {ID_O:['O_water', 'O_water'], ID_H:['H_water', 'H_water']}}
    }

    bond_dict = {
    # TIP4P is a rigid model (use fix shake), force constants should just be reasonable values
    # TIP3P has force constants if a flexible model is desired
    'TIP4P_cutoff':      {BT: {'style':'harmonic', 'params':(100.0, 0.9572), 'comments':'# O_water H_water'}},
    'TIP4P_2005_cutoff': {BT: {'style':'harmonic', 'params':(100.0, 0.9572), 'comments':'# O_water H_water'}},
    'TIP4P_2005_long':   {BT: {'style':'harmonic', 'params':(100.0, 0.9572), 'comments':'# O_water H_water'}},
    'TIP3P_long':        {BT: {'style':'harmonic', 'params':(450.0, 0.9572), 'comments':'# O_water H_water'}} 
    }

    angle_dict = {
    # TIP4P is a rigid model (use fix shake), force constants should just be reasonable values
    # TIP3P has force constants if a flexible model is desired
    'TIP4P_cutoff':      {AT: {'style':'harmonic', 'params':(50.0, 104.52), 'comments':'# H_water O_water H_water'}},
    'TIP4P_2005_cutoff': {AT: {'style':'harmonic', 'params':(50.0, 104.52), 'comments':'# H_water O_water H_water'}},
    'TIP4P_2005_long':   {AT: {'style':'harmonic', 'params':(50.0, 104.52), 'comments':'# H_water O_water H_water'}},
    'TIP3P_long':        {AT: {'style':'harmonic', 'params':(55.0, 104.52), 'comments':'# H_water O_water H_water'}}
    }

    qO,qH = charge_dict[model]
    LJ_params = LJ_dict[model]
    bond_params = bond_dict[model]
    angle_params = angle_dict[model]

    if 'TIP4P' in model:

        molfile = dedent("""# Water molecule. useable for TIP3P or TIP4P in LAMMPS.

3 atoms
2 bonds
1 angles

Coords

1    1.12456   0.09298   1.27452
2    1.53683   0.75606   1.89928
3    0.49482   0.56390   0.65678

Types

1    {ID_O}
2    {ID_H}
3    {ID_H}

Charges

1    {qO}
2    {qH}
3    {qH}

Bonds

1    {BT} 1 2
2    {BT} 1 3

Angles

1    {AT} 2 1 3

Shake Flags

1 1
2 1
3 1

Shake Atoms

1 1 2 3
2 1 2 3
3 1 2 3

Shake Bond Types

1 {BT} {BT} {AT}
2 {BT} {BT} {AT}
3 {BT} {BT} {AT}""".format(**locals())).strip()

    if 'TIP3P' in model:
        
        molfile = dedent("""# Water molecule. useable for TIP3P or TIP4P in LAMMPS.

3 atoms
2 bonds
1 angles

Coords

1    1.12456   0.09298   1.27452
2    1.53683   0.75606   1.89928
3    0.49482   0.56390   0.65678

Types

1    {ID_O}
2    {ID_H}
3    {ID_H}

Charges

1    {qO}
2    {qH}
3    {qH}

Bonds

1    {BT} 1 2
2    {BT} 1 3

Angles

1    {AT} 2 1 3""".format(**locals())).strip()

    mass_dict = {ID_O:15.9994, ID_H:1.00794}
    molnames = ('H2O_mol', 'H2O.txt')

    extra_types = (2,1,1,None,None)

    return molfile, LJ_params, bond_params, angle_params, molnames, mass_dict, M_site_dist_dict[model], extra_types

#------------------------------------------------------------------------------------------------------------------
from small_molecule_constants import TraPPE
def MX2(last_atom_ID, last_bond_ID, last_angle_ID, molname, model):
    print("read molecular parameters: ",molname)
    MX2_data = TraPPE[molname]
    #--------------------------------------------------------------------------
    pair_style   = MX2_data['pair']['style']
    print(f"Pair style: {pair_style}")
    #--------------------------------------------------------------------------
    vdW_params   = MX2_data['pair']['vdW']
    #for specific_vdW, vdW_value in vdW_params.items():
    #    print(f"vdW: {specific_vdW}, Value: {vdW_value}")
    vdW_keys = []
    epsilon_values = []
    sigma_values = []
    
    for specific_vdW, vdW_value in vdW_params.items():
        vdW_keys.append(specific_vdW)
        epsilon_values.append(vdW_value[0])
        sigma_values.append(vdW_value[1])
    
    print(f"vdW Keys: {vdW_keys}")
    print(f"Epsilon Values: {epsilon_values}")
    print(f"Sigma Values: {sigma_values}")
    #--------------------------------------------------------------------------
    charges      = MX2_data['pair']['charges']
    #for specific_charge, charge_value in charges.items():
    #    print(f"Charge: {specific_charge}, Value: {charge_value}")
    charge_keys = []
    charge_values = []
    
    for specific_charge, charge_value in charges.items():
        charge_keys.append(specific_charge)
        charge_values.append(charge_value)
    
    print(f"Charge Keys: {charge_keys}")
    print(f"Charge Values: {charge_values}")
    #--------------------------------------------------------------------------
    bond_params  = MX2_data['bonds']
    
    specific_bond, first_params = next(iter(bond_params.items()))
    specific_bond_str = ' '.join(map(str, specific_bond))
    bond_style = first_params[0]
    bond_k = first_params[1]
    bond_r0 = first_params[2]
    
    print(f"Bond: {specific_bond}, Style: {bond_style}, bond_k: {bond_k}, bond_r0: {bond_r0}")
    #--------------------------------------------------------------------------
    angle_params = MX2_data['angles']
    
    specific_angle, first_params = next(iter(angle_params.items()))
    specific_angle_str = ' '.join(map(str, specific_angle))
    angle_style = first_params[0]
    angle_k = first_params[1]
    angle_theta0 = first_params[2]
    
    print(f"Angle: {specific_angle}, Style: {angle_style}, angle_k: {angle_k}, angle_theta0: {angle_theta0}")
    #--------------------------------------------------------------------------
    masses      = MX2_data['mass']
    for specific_mass, mass_value in masses.items():
        print(f"Mass: {specific_mass}, Value: {mass_value}")
    mass_keys = []
    mass_values = []
    
    for specific_mass, mass_value in masses.items():
        mass_keys.append(specific_mass)
        mass_values.append(mass_value)
    
    print(f"mass Keys: {mass_keys}")
    print(f"mass Values: {mass_values}")
    #--------------------------------------------------------------------------

    ID_M = last_atom_ID + 1
    ID_X = ID_M + 1

    BT = last_bond_ID + 1
    AT = last_angle_ID + 1

    charge_dict = {
    'TraPPE': charge_values
    }

    M_site_dist_dict = {
    'TraPPE': None
    }

    LJ_dict = {
    # LAMMPS has a special TIP4P pair_style that automatically adds the M site
    'TraPPE': {ID_X: (pair_style , epsilon_values[0], sigma_values[0]), ID_M: (pair_style , epsilon_values[1], sigma_values[1]), 'style': pair_style , 'comments': {ID_X: vdW_keys[0], ID_M: vdW_keys[1]}}
    }

    bond_dict = {
    'TraPPE': {BT: {'style':bond_style, 'params':(bond_k, bond_r0), 'comments':"# "+specific_bond_str}}
    }

    angle_dict = {
    'TraPPE': {AT: {'style':angle_style, 'params':(angle_k, angle_theta0), 'comments':"# "+specific_angle_str}}
    }

    qX,qM = charge_dict[model]
    LJ_params = LJ_dict[model]
    bond_params = bond_dict[model]
    angle_params = angle_dict[model]
    
    print(f"----------------------------- ----------------------------- -----------------------------")
    print(f"qX: {qX}, qM: {qM}")
    print(f"LJ_params: {LJ_params}")
    print(f"bond_params: {bond_params}")
    print(f"angle_params: {angle_params}")
    print(f"----------------------------- ----------------------------- -----------------------------")

    if 'TraPPE' in model:

        molfile = dedent("""# MX2 molecule. useable for TraPPE in LAMMPS.

3 atoms
2 bonds
1 angles

Coords

1    0.00000   0.00000   0.00000
2    0.00000   0.00000  -{bond_r0}
3    0.00000   0.00000  +{bond_r0}

Types

1    {ID_M}
2    {ID_X}
3    {ID_X}

Charges

1    {qM}
2    {qX}
3    {qX}

Bonds

1    {BT} 1 2
2    {BT} 1 3

Angles

1    {AT} 2 1 3

Shake Flags

1 1
2 1
3 1

Shake Atoms

1 1 2 3
2 1 2 3
3 1 2 3

Shake Bond Types

1 {BT} {BT} {AT}
2 {BT} {BT} {AT}
3 {BT} {BT} {AT}""".format(**locals())).strip()

    mass_dict = {ID_M:mass_values[1], ID_X:mass_values[0]}
    molnames = ('MX2_mol', 'MX2.txt')

    extra_types = (2,1,1,None,None)

    return molfile, LJ_params, bond_params, angle_params, molnames, mass_dict, M_site_dist_dict[model], extra_types
