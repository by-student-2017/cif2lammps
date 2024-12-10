# The Siepmann Group: http://trappe.oit.umn.edu/
# M. Barraco et al., J. Phys. Chem. A 2023, 127, 30, 6335-6346.:  https://doi.org/10.1021/acs.jpca.3c03212
# vdW:kcal/mol, Angstrom
# 1 [K] -> 1.380649e-23/4184*6.022e22 [kcal/mol]
TraPPE =  {
    'O2': { # oxygen (small)
        'pair': {
            'style': 'lj/cut/coul/long', 
            'vdW': {'O_O2': (0.0974,3.02), 'O_com': (0.0,0.0)},  # epsilon NN/kB = 49.0 K = 0.0974 kcal/mol, sigma of NN = 3.02 Angstrom
            'charges': {'O_O2': -0.113, 'O_com': 0.226} # q/e = -0.113 on N atoms, countercharge on COM (M)
        },
        'bonds': {('O_O2', 'O_com'): ('harmonic',1200.0,0.605)}, # molecule should be kept rigid, force constants don't matter (# O-O bond length = 1.21 Angstrom)
        'angles': {('O_O2', 'O_com', 'O_O2'): ('harmonic',500.0,180.0)}, # molecule should be kept rigid, force constants don't matter
        'dihedrals': None,
        'impropers': None,
        'mass': {'O_O2': 15.9994, 'O_com': 0.1}
    },
    'N2': { # nitrogen (small)
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'N_N2': (0.0715, 3.31),'N_com': (0.0,0.0)}, # epsilon NN/kB = 36.0 K = 0.0715 kcal/mol, sigma of NN = 3.31 Angstrom
            'charges': {'N_N2': -0.482, 'N_com': 0.964}  # q/e = -0.482 on N atoms, countercharge on COM (M)
        },
        'bonds': {('N_com', 'N_com'): ('harmonic', 5000.0, 0.550)},  # N-N bond length = 1.10 Angstrom (The value is set at 5000.0 to reflect the strength of the triple bond in the N2 molecule.)
        'angles': {('N_N2', 'N_com', 'N_N2'): ('harmonic',500.0,180.0)}, # molecule should be kept rigid, force constants don't matter
        'dihedrals': None,
        'impropers': None,
        'mass': {'N_N2': 14.007, 'N_com': 0.1}
    },
    'H2': { # H2-LJ-2S-q+/- TraPPE model
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'H_H2': (0.0016, 3.03), 'H_com': (0.0,0.0)},  # epsilon HH/kB = 8.06 K = 0.00160 kcal/mol, sigma of HH = 3.03 Angstrom
            'charges': {'H_H2': 0.47, 'H_com': -0.94}  # q/e = 0.47 on H atoms, countercharge on COM (M)
        },
        'bonds': {('H_H2', 'H_com'): ('harmonic', 550.0, 0.3705)},  # H-H bond length = 0.741 Angstrom
        'angles': {('H_H2', 'H_com', 'H_H2'): ('harmonic',500.0,180.0)}, # molecule should be kept rigid, force constants don't matter
        'dihedrals': None,
        'impropers': None,
        'mass': {'H_H2': 1.00794, 'H_com': 0.1}
    },
    #'H2': {
    #    'pair': {
    #        'style': 'lj/cut/coul/long',
    #        'vdW': {'H_H2': (0.0460, 2.958)},
    #        'charges': {'H_H2': 0.0}
    #    },
    #    'bonds': {('H_H2', 'H_H2'): ('harmonic', 100.0, 0.74)},
    #    'angles': None,
    #    'dihedrals': None,
    #    'impropers': None
    #},
    #'T2': {  # tritium (dummy)
    #    'pair': {
    #        'style': 'lj/cut/coul/long',
    #        'vdW': {'T_T2': (0.0200, 2.96)},
    #        'charges': {'T_T2': 0.0}
    #    },
    #    'bonds': {('T_T2', 'T_T2'): ('harmonic', 100.0, 0.74)},
    #    'angles': None,
    #    'dihedrals': None,
    #    'impropers': None
    #},
    'H2O': { # SPC-pol3 (pol)
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'O_w': (0.2683, 2.665), 'H_w': (0.0, 0.0)},
            'charges': {'O_w': -0.672, 'H_w': 0.336}
        },
        'bonds': {('O_w', 'H_w'): ('harmonic', 450.0, 1.0)},
        'angles': {('H_w', 'O_w', 'H_w'): ('harmonic', 55.0, 109.47)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'O_w': 15.9994, 'H_w': 1.00794}
    },
    'CO': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_CO': (0.055, 3.75), 'O_CO': (0.170, 3.05)},
            'charges': {'C_CO': 0.48, 'O_CO': -0.48}
        },
        'bonds': {('C_CO', 'O_CO'): ('harmonic', 100.0, 1.128)},
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'NO': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'N_NO': (0.0690, 3.31), 'O_NO': (0.0974, 3.02)},
            'charges': {'N_NO': 0.0, 'O_NO': 0.0}
        },
        'bonds': {('N_NO', 'O_NO'): ('harmonic', 100.0, 1.15)},
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'CO2': { # carbon dioxide (small)
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_CO2': (0.00537, 2.800), 'O_CO2': (0.1570, 3.050)},
            'charges': {'C_CO2': 0.70, 'O_CO2': -0.35}
        },
        'bonds': {('C_CO2', 'O_CO2'): ('harmonic', 5000.0, 1.16)},
        'angles': {('O_CO2', 'C_CO2', 'O_CO2'): ('harmonic', 500.0, 180.0)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'C_CO2': 12.011, 'O_CO2': 15.9994}
    },
    'NO2': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'N_NO2': (0.0690, 3.31), 'O_NO2': (0.0974, 3.02)},
            'charges': {'N_NO2': 0.46, 'O_NO2': -0.23}
        },
        'bonds': {('N_NO2', 'O_NO2'): ('harmonic', 100.0, 1.20)},
        'angles': {('O_NO2', 'N_NO2', 'O_NO2'): ('harmonic', 100.0, 134.0)},
        'dihedrals': None,
        'impropers': None
    },
    'SO2': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_SO2': (0.250, 3.60), 'O_SO2': (0.170, 3.05)},
            'charges': {'S_SO2': 0.64, 'O_SO2': -0.32}
        },
        'bonds': {('S_SO2', 'O_SO2'): ('harmonic', 100.0, 1.43)},
        'angles': {('O_SO2', 'S_SO2', 'O_SO2'): ('harmonic', 100.0, 119.5)},
        'dihedrals': None,
        'impropers': None
    },
    'SO3': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_SO3': (0.250, 3.60), 'O_SO3': (0.0974, 3.02)},
            'charges': {'S_SO3': 1.5, 'O_SO3': -0.5}
        },
        'bonds': {('S_SO3', 'O_SO3'): ('harmonic', 100.0, 1.43)},
        'angles': {('O_SO3', 'S_SO3', 'O_SO3'): ('harmonic', 100.0, 120.0)},
        'dihedrals': None,
        'impropers': None
    },
    'SF6': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_SF6': (0.0910, 4.0), 'F_SF6': (0.0300, 3.0)},
            'charges': {'S_SF6': 0.0, 'F_SF6': 0.0}
        },
        'bonds': {('S_SF6', 'F_SF6'): ('harmonic', 100.0, 1.56)},
        'angles': {('F_SF6', 'S_SF6', 'F_SF6'): ('harmonic', 100.0, 90.0)},
        'dihedrals': None,
        'impropers': None
    },
    'H2S': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_H2S': (0.1000, 3.60), 'H_H2S': (0.0200, 2.50)},
            'charges': {'S_H2S': -0.34, 'H_H2S': 0.17}
        },
        'bonds': {('S_H2S', 'H_H2S'): ('harmonic', 100.0, 1.34)},
        'angles': {('H_H2S', 'S_H2S', 'H_H2S'): ('harmonic', 100.0, 92.1)},
        'dihedrals': None,
        'impropers': None
    },
    'HCN': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'H_HCN': (0.0300, 2.42), 'C_HCN': (0.1050, 3.40), 'N_HCN': (0.0690, 3.31)},
            'charges': {'H_HCN': 0.19, 'C_HCN': -0.27, 'N_HCN': 0.08}
        },
        'bonds': {('H_HCN', 'C_HCN'): ('harmonic', 100.0, 1.06), ('C_HCN', 'N_HCN'): ('harmonic', 100.0, 1.16)},
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'CN2': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_CN2': (0.1050, 3.40), 'N_CN2': (0.0690, 3.31)},
            'charges': {'C_CN2': 0.0, 'N_CN2': 0.0}
        },
        'bonds': {('C_CN2', 'N_CN2'): ('harmonic', 100.0, 1.16)},
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'NH3': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'N_NH3': (0.200, 3.30), 'H_NH3': (0.0, 0.0)},
            'charges': {'N_NH3': -0.82, 'H_NH3': 0.27}
        },
        'bonds': {('N_NH3', 'H_NH3'): ('harmonic', 100.0, 1.01)},
        'angles': {('H_NH3', 'N_NH3', 'H_NH3'): ('harmonic', 100.0, 107.8)},
        'dihedrals': None,
        'impropers': None
    },
    'CH4': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_CH4': (0.294, 3.73)}, # epsilon NN/kB = 148.0 K = 0.0715 kcal/mol, sigma of NN = 3.73 Angstrom
            'charges': {'C_CH4': 0.0} # q/e = 0.0
        },
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'propane': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_C3': (0.0910, 3.75), 'H_C3': (0.0150, 2.50)},
            'charges': {'C_C3': -0.27, 'H_C3': 0.09}
        },
        'bonds': {('C_C3', 'H_C3'): ('harmonic', 100.0, 1.09), ('C_C3', 'C_C3'): ('harmonic', 100.0, 1.54)},
        'angles': {('H_C3', 'C_C3', 'H_C3'): ('harmonic', 100.0, 109.5), ('H_C3', 'C_C3', 'C_C3'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'propylene': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_C3': (0.0910, 3.75), 'H_C3': (0.0150, 2.50), 'C_C2': (0.0910, 3.75)},
            'charges': {'C_C3': -0.27, 'H_C3': 0.09, 'C_C2': -0.27}
        },
        'bonds': {('C_C3', 'H_C3'): ('harmonic', 100.0, 1.09), ('C_C3', 'C_C3'): ('harmonic', 100.0, 1.54), ('C_C3', 'C_C2'): ('harmonic', 100.0, 1.34)},
        'angles': {('H_C3', 'C_C3', 'H_C3'): ('harmonic', 100.0, 109.5), ('H_C3', 'C_C3', 'C_C3'): ('harmonic', 100.0, 109.5), ('C_C3', 'C_C2', 'H_C3'): ('harmonic', 100.0, 120.0)},
        'dihedrals': None,
        'impropers': None
    },
    '2-methylbutane': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_C3': (0.0910, 3.75), 'H_C3': (0.0150, 2.50)},
            'charges': {'C_C3': -0.27, 'H_C3': 0.09}
        },
        'bonds': {('C_C3', 'H_C3'): ('harmonic', 100.0, 1.09), ('C_C3', 'C_C3'): ('harmonic', 100.0, 1.54)},
        'angles': {('H_C3', 'C_C3', 'H_C3'): ('harmonic', 100.0, 109.5), ('H_C3', 'C_C3', 'C_C3'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    '23-dimethylbutane': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_C3': (0.0910, 3.75), 'H_C3': (0.0150, 2.50)},
            'charges': {'C_C3': -0.27, 'H_C3': 0.09}
        },
        'bonds': {('C_C3', 'H_C3'): ('harmonic', 100.0, 1.09), ('C_C3', 'C_C3'): ('harmonic', 100.0, 1.54)},
        'angles': {('H_C3', 'C_C3', 'H_C3'): ('harmonic', 100.0, 109.5), ('H_C3', 'C_C3', 'C_C3'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'butane': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_C3': (0.0910, 3.75), 'H_C3': (0.0150, 2.50)},
            'charges': {'C_C3': -0.27, 'H_C3': 0.09}
        },
        'bonds': {('C_C3', 'H_C3'): ('harmonic', 100.0, 1.09), ('C_C3', 'C_C3'): ('harmonic', 100.0, 1.54)},
        'angles': {('H_C3', 'C_C3', 'H_C3'): ('harmonic', 100.0, 109.5), ('H_C3', 'C_C3', 'C_C3'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'ethane': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_C2': (0.0910, 3.75), 'H_C2': (0.0150, 2.50)},
            'charges': {'C_C2': -0.27, 'H_C2': 0.09}
        },
        'bonds': {('C_C2', 'H_C2'): ('harmonic', 100.0, 1.09), ('C_C2', 'C_C2'): ('harmonic', 100.0, 1.54)},
        'angles': {('H_C2', 'C_C2', 'H_C2'): ('harmonic', 100.0, 109.5), ('H_C2', 'C_C2', 'C_C2'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'heptane': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_C3': (0.0910, 3.75), 'H_C3': (0.0150, 2.50)},
            'charges': {'C_C3': -0.27, 'H_C3': 0.09}
        },
        'bonds': {('C_C3', 'H_C3'): ('harmonic', 100.0, 1.09), ('C_C3', 'C_C3'): ('harmonic', 100.0, 1.54)},
        'angles': {('H_C3', 'C_C3', 'H_C3'): ('harmonic', 100.0, 109.5), ('H_C3', 'C_C3', 'C_C3'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'hexane': {
        'pair': {'style': 'lj/cut/coul/long', 'vdW': {'C_hexane': (0.0910, 3.75), 'H_hexane': (0.0152, 2.50)}, 'charges': {'C_hexane': 0.0, 'H_hexane': 0.0}},
        'bonds': {('C_hexane', 'H_hexane'): ('harmonic', 100.0, 1.09)},
        'angles': {('H_hexane', 'C_hexane', 'H_hexane'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'methane': {
        'pair': {'style': 'lj/cut/coul/long', 'vdW': {'C_methane': (0.0910, 3.75), 'H_methane': (0.0152, 2.50)}, 'charges': {'C_methane': 0.0, 'H_methane': 0.0}},
        'bonds': {('C_methane', 'H_methane'): ('harmonic', 100.0, 1.09)},
        'angles': {('H_methane', 'C_methane', 'H_methane'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'nonane': {
        'pair': {'style': 'lj/cut/coul/long', 'vdW': {'C_nonane': (0.0910, 3.75), 'H_nonane': (0.0152, 2.50)}, 'charges': {'C_nonane': 0.0, 'H_nonane': 0.0}},
        'bonds': {('C_nonane', 'H_nonane'): ('harmonic', 100.0, 1.09)},
        'angles': {('H_nonane', 'C_nonane', 'H_nonane'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'octane': {
        'pair': {'style': 'lj/cut/coul/long', 'vdW': {'C_octane': (0.0910, 3.75), 'H_octane': (0.0152, 2.50)}, 'charges': {'C_octane': 0.0, 'H_octane': 0.0}},
        'bonds': {('C_octane', 'H_octane'): ('harmonic', 100.0, 1.09)},
        'angles': {('H_octane', 'C_octane', 'H_octane'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'pentane': {
        'pair': {'style': 'lj/cut/coul/long', 'vdW': {'C_pentane': (0.0910, 3.75), 'H_pentane': (0.0152, 2.50)}, 'charges': {'C_pentane': 0.0, 'H_pentane': 0.0}},
        'bonds': {('C_pentane', 'H_pentane'): ('harmonic', 100.0, 1.09)},
        'angles': {('H_pentane', 'C_pentane', 'H_pentane'): ('harmonic', 100.0, 109.5)},
        'dihedrals': None,
        'impropers': None
    },
    'Ar': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Ar_Ar': (0.238, 3.40)},
            'charges': {'Ar_Ar': 0.0}
        },
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'Ne': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Ne_Ne': (0.032, 2.79)},
            'charges': {'Ne_Ne': 0.0}
        },
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'He': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'He_He': (0.084, 2.64)},
            'charges': {'He_He': 0.0}
        },
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'Kr': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Kr_Kr': (0.283, 3.63)},
            'charges': {'Kr_Kr': 0.0}
        },
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    },
    'Xe': {
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Xe_Xe': (0.364, 3.96)},
            'charges': {'Xe_Xe': 0.0}
        },
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    }
}

TIP4P_2005_long =  {
# this is TIP4P/2005 water, should be used with long-range electrostatics with 8.5 Å cutoff and fix/shake
# keep in mind that using any long pair_style in lammps will include long-range electrostatics FOR ALL ATOMS in the simulation
    'H2O1': {
        'pair': {'style': 'lj/cut/tip4p/long', 'vdW': {'H_w': (0.0,1.0), 'O_w': (0.1852, 3.1589)}, 'charges': {'H_w': 0.5564, 'O_w': -1.1128}},
        'bonds': {('H_w', 'O_w'): ('harmonic', 450.0, 0.9572)},
        'angles': {('H_w', 'O_w', 'H_w'): ('harmonic', 55.0, 104.52)},
        'dihedrals': None,
        'impropers': None
    },
    'Cl1': {
        'pair': {'style': 'lj/cut/tip4p/long', 'vdW': {'Cl_Cl1': (0.22700, 3.51638)}, 'charges': {'Cl_Cl1': -1.0}},
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    }
}

TIP4P_2005_cutoff =  {
# this is TIP4P/2005 water but with no long range electrostatics
    'H2O1': {
        'pair': {'style': 'lj/cut/tip4p/cut', 'vdW': {'H_w': (0.0,0.0), 'O_w': (0.1852, 3.1589)}, 'charges': {'H_w': 0.5564, 'O_w': -1.1128}},
        'bonds': {('H_w', 'O_w'): ('harmonic', 450.0, 0.9572)},
        'angles': {('H_w', 'O_w', 'H_w'): ('harmonic', 55.0, 104.52)},
        'dihedrals': None,
        'impropers': None
    },
    'Cl1': {
        'pair': {'style': 'lj/cut/tip4p/long', 'vdW': {'Cl_Cl1': (0.22700, 3.51638)}, 'charges': {'Cl_Cl1': -1.0}},
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    }
}

TIP4P_cutoff =  {
# this is the original TIP4P water model
    'H2O1': {
        'pair': {'style': 'lj/cut/tip4p/cut', 'vdW': {'H_w': (0.0,0.0), 'O_w': (0.1550, 3.1536)}, 'charges': {'H_w': 0.5200, 'O_w': -1.040}},
        'bonds': {('H_w', 'O_w'): ('harmonic', 450.0, 0.9572)},
        'angles': {('H_w', 'O_w', 'H_w'): ('harmonic', 55.0, 104.52)},
        'dihedrals': None,
        'impropers': None
    },
    'Cl1': {
        'pair': {'style': 'lj/cut/tip4p/cut', 'vdW': {'Cl_Cl1': (0.22700, 3.51638)}, 'charges': {'Cl_Cl1': -1.0}},
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    }
}

Ions =  {
    'Cl1': {
        'pair': {'style': 'lj/cut/coul/long', 'vdW': {'Cl_Cl1': (0.22700, 3.51638)}, 'charges': {'Cl_Cl1': -1.0}},
        'bonds': None,
        'angles': None,
        'dihedrals': None,
        'impropers': None
    }
}