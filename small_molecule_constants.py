# The Siepmann Group: http://trappe.oit.umn.edu/
# M. Barraco et al., J. Phys. Chem. A 2023, 127, 30, 6335-6346.:  https://doi.org/10.1021/acs.jpca.3c03212
# vdW:kcal/mol, Angstrom
# 1 [K] = 1.380649e-23/4184*6.022e22 [kcal/mol]
# 1 [kJ/mol] = 0.23900574 [kcal/mol]
TraPPE =  { # O2, N2, H2, H2S, H2O, CO2, NO2, SO2
    'O2': { # oxygen (small)
        'pair': {
            'style': 'lj/cut/coul/long', 
            'vdW': {'O_O2': (0.0974,3.02), 'O_com': (0.0,0.0)},  # epsilon NN/kB = 49.0 K = 0.0974 kcal/mol, sigma of NN = 3.02 Angstrom
            'charges': {'O_O2': -0.113, 'O_com': 0.226} # q/e = -0.113 on N atoms, countercharge on COM (M)
        },
        'bonds': {('O_O2', 'O_com'): ('harmonic', 70.25, 0.605)}, # molecule should be kept rigid, force constants don't matter (# O-O bond length = 1.21 Angstrom)
        'angles': {('O_O2', 'O_com', 'O_O2'): ('harmonic', 281, 180.0)}, # molecule should be kept rigid, force constants don't matter
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
        'bonds': {('N_com', 'N_com'): ('harmonic', 137, 0.550)},  # N-N bond length = 1.10 Angstrom (The value is set at 5000.0 to reflect the strength of the triple bond in the N2 molecule.)
        'angles': {('N_N2', 'N_com', 'N_N2'): ('harmonic', 550.0, 180.0)}, # molecule should be kept rigid, force constants don't matter
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
        'bonds': {('H_H2', 'H_com'): ('harmonic', 34.25, 0.3705)},  # H-H bond length = 0.741 Angstrom
        'angles': {('H_H2', 'H_com', 'H_H2'): ('harmonic', 137, 180.0)}, # molecule should be kept rigid, force constants don't matter
        'dihedrals': None,
        'impropers': None,
        'mass': {'H_H2': 1.00794, 'H_com': 0.1}
    },
    'F2': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'F_F2': (0.0298, 3.40), 'F_com': (0.0,0.0)},
            'charges': {'F_F2': 0.0, 'F_com': 0.0}
        },
        'bonds': {('F_F2', 'F_com'): ('harmonic', 8.335, 0.7055)},
        'angles': {('F_F2', 'F_com', 'F_F2'): ('harmonic', 33.4, 180.0)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'F_F2': 18.998, 'F_com': 0.0}
    },
    'Cl2': { # dummy, Uses: Disinfection and sterilization, bleach, chemical industry, pesticide manufacturing, pharmaceutical manufacturing
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Cl_Cl2': (0.368, 4.12), 'Cl_com': (0.0,0.0)},
            'charges': {'Cl_Cl2': 0.0, 'Cl_com': 0.0}
        },
        'bonds': {('Cl_Cl2', 'Cl_com'): ('harmonic', 15.6, 0.49675)},
        'angles': {('Cl_Cl2', 'Cl_com', 'Cl_Cl2'): ('harmonic', 62.5, 180.0)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'Cl_Cl2': 35.453, 'Cl_com': 0.1}
    },
    # H2S: Applications: industrial production, environmental protection, medical research
    'H2S': { # 3-3 model: M. S. Shah et al., J. Phys. Chem. B 2015, 119, 23, 7041-7052.: https://doi.org/10.1021/acs.jpcb.5b02536
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_H2S': (0.0248, 3.60), 'H_H2S': (0.0072, 2.50)},
            'charges': {'S_H2S': -0.28, 'H_H2S': 0.14} # The 4-3 model is better, but the structure is more complicated. Therefore, I chose the 3-3, which is the next best option.
        },
        'bonds': {('S_H2S', 'H_H2S'): ('harmonic', 100.0, 1.34)},
        'angles': {('H_H2S', 'S_H2S', 'H_H2S'): ('harmonic', 100.0, 92)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'S_H2S': 32.06, 'H_H2S': 1.00794}
    },
    'H2Se': { # dummy, Uses: Synthesis of organic selenium compounds, semiconductor manufacturing
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Se_H2Se': (0.210, 4.10), 'H_H2Se': (0.0072, 2.50)},
            'charges': {'Se_H2Se': -0.40, 'H_H2Se': 0.20}
        },
        'bonds': {('Se_H2Se', 'H_H2Se'): ('harmonic', 110.0, 1.47)},
        'angles': {('H_H2Se', 'Se_H2Se', 'H_H2Se'): ('harmonic', 105.0, 91.5)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'Se_H2Se': 78.96, 'H_H2Se': 1.00794}
    },
    'H2Te': { # dummy, Uses: Semiconductor manufacturing
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Se_H2Se': (0.210, 4.10), 'H_H2Se': (0.0072, 2.50)},
            'charges': {'Te_H2Te': -0.40, 'H_H2Te': 0.20}
        },
        'bonds': {('Te_H2Te', 'H_H2Te'): ('harmonic', 115.0, 1.50)},
        'angles': {('H_H2Te', 'Te_H2Te', 'H_H2Te'): ('harmonic', 110.0, 90.5)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'Te_H2Te': 127.60, 'H_H2Te': 1.00794}
    },
    'ClO2': { # dummy, Uses: Disinfection and sterilization
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'Cl_ClO2': (0.0147, 3.39), 'O_ClO2': (0.0157, 3.05)},
            'charges': {'Cl_ClO2': 0.42, 'O_ClO2': -0.21}
        },
        'bonds': {('Cl_ClO2', 'O_ClO2'): ('harmonic', 130.0, 1.56)},
        'angles': {('O_ClO2', 'Cl_ClO2', 'O_ClO2'): ('harmonic', 12.0, 116.5)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'Cl_ClO2': 35.453, 'O_ClO2': 15.9994}
    },
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
    'NO2': { # S. Thompho et al., ACS Omega 2021, 6, 27, 17342-17352.: https://doi.org/10.1021/acsomega.1c01459
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'N_NO2': (0.0690, 3.240), 'O_NO2': (0.0974, 2.930)}, # N:0.4174 [kJ/mol],3.240 [A], O:0.5179 [kJ/mol], 2.930 [A]
            'charges': {'N_NO2': 0.146, 'O_NO2': -0.073}
        },
        'bonds': {('N_NO2', 'O_NO2'): ('harmonic', 89.0, 1.20)},
        'angles': {('O_NO2', 'N_NO2', 'O_NO2'): ('harmonic', 1.5, 134.1)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'N_NO2': 14.007, 'O_NO2': 15.9994}
    },
    'SO2': { # G. Kamath et al., J. Chem. Phys. 136, 044514 (2012): https://doi.org/10.1063/1.3677880
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_SO2': (0.0147, 3.39), 'O_SO2': (0.0157, 3.05)}, # S:73.8 [K], 3.39 [A], O:79.0 [K], 3.05 [A]
            'charges': {'S_SO2': 0.59, 'O_SO2': -0.295}
        },
        'bonds': {('S_SO2', 'O_SO2'): ('harmonic', 125.0, 1.43)},
        'angles': {('O_SO2', 'S_SO2', 'O_SO2'): ('harmonic', 11.0, 119.3)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'S_SO2': 32.06, 'O_SO2': 15.9994}
    },
    'SCl2': { # dummy, Uses: organic synthesis, intermediates for pesticides, high pressure lubricants, disinfectants and sterilizers, chlorination agents
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_SCl2': (0.276, 3.55), 'Cl_SCl2': (0.265, 3.40)},
            'charges': {'S_SCl2': 0.50, 'Cl_SCl2': -0.25}
        },
        'bonds': {('S_SCl2', 'Cl_SCl2'): ('harmonic', 250.0, 2.07)},
        'angles': {('Cl_SCl2', 'S_SCl2', 'Cl_SCl2'): ('harmonic', 60.0, 103.0)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'S_SCl2': 32.06, 'Cl_SCl2': 35.453}
    },
    'SF2': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'S_SF2': (0.276, 3.55), 'F_SF2': (0.061, 3.12)},
            'charges': {'S_SF2': 0.50, 'F_SF2': -0.25}
        },
        'bonds': {('S_SF2', 'F_SF2'): ('harmonic', 300.0, 1.56)},
        'angles': {('F_SF2', 'S_SF2', 'F_SF2'): ('harmonic', 70.0, 98.0)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'S_SF2': 32.06, 'F_SF2': 18.998}
    },
    'PCl2': { # dummy, Uses: Organic synthesis, intermediate for pesticides
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'P_PCl2': (0.276, 3.55), 'Cl_PCl2': (0.265, 3.40)},
            'charges': {'P_PCl2': 0.50, 'Cl_PCl2': -0.25}
        },
        'bonds': {('P_PCl2', 'Cl_PCl2'): ('harmonic', 250.0, 2.07)},
        'angles': {('Cl_PCl2', 'P_PCl2', 'Cl_PCl2'): ('harmonic', 60.0, 103.0)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'P_PCl2': 30.97, 'Cl_PCl2': 35.453}
    },
    'PF2': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'P_PF2': (0.276, 3.55), 'F_PF2': (0.061, 3.12)},
            'charges': {'P_PF2': 0.50, 'F_PF2': -0.25}
        },
        'bonds': {('P_PF2', 'F_PF2'): ('harmonic', 300.0, 1.56)},
        'angles': {('F_PF2', 'P_PF2', 'F_PF2'): ('harmonic', 70.0, 98.0)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'P_PF2': 30.97, 'F_PF2': 18.998}
    },
    'CN2': { # dummy
        'pair': {
            'style': 'lj/cut/coul/long',
            'vdW': {'C_CN2': (0.0072, 3.40), 'N_CN2': (0.0072, 3.3)},
            'charges': {'C_CN2': 0.70, 'N_CN2': -0.35}
        },
        'bonds': {('C_CN2', 'N_CN2'): ('harmonic', 6.29, 1.16)},
        'angles': {('N_CN2', 'C_CN2', 'N_CN2'): ('harmonic', 1.715, 120)},
        'dihedrals': None,
        'impropers': None,
        'mass': {'C_CN2': 12.011, 'N_CN2': 14.007}
    },
    #--------------------------------------------------------------------------------------------------------
    # The following structures are not yet in place:
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