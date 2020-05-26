# I am aware I have not followed the Python syntax guidlines for this data entry, but it 
# really makes things easier to have justified columns -Ryther

# UFF and UFF4MOF parameters are taken directly from gulp-5.1 (uff4mof.lib)

UFF4MOF_atom_parameters = {
# type    r0     theta_0   x_i     D_i     zeta    Z_i     Vi/Uj   Xi       
"H_"   : (0.354, 180.0   , 2.886,  0.044,  12.0  , 0.7120, 0.000,  4.528),
"H_b"  : (0.460,  83.5   , 2.886,  0.044,  12.0  , 0.7125, 0.000,  4.528),
"He4+4": (0.849,  90.0   , 2.362,  0.056,  15.24 , 0.0972, 0.000,  9.660),
"Li"   : (1.336, 180.0   , 2.451,  0.025,  12.0  , 1.0255, 0.000,  3.006),
"Li3f2": (1.280, 109.4712, 2.451,  0.025,  12.0  , 1.0255, 0.000,  3.006),
"Be3+2": (1.074, 109.4712, 2.745,  0.085,  12.0  , 1.5650, 0.000,  4.877),
"B_3"  : (0.838, 109.4712, 4.083,  0.180,  12.052, 1.7550, 0.000,  4.068),
"B_2"  : (0.828, 120.0   , 4.083,  0.180,  12.052, 1.7550, 2.000,  4.068),
"C_3"  : (0.757, 109.4712, 3.851,  0.105,  12.73 , 1.9120, 2.119,  5.343),
"C_R"  : (0.729, 120.0   , 3.851,  0.105,  12.73 , 1.9120, 2.000,  5.343),
"C_2"  : (0.732, 120.0   , 3.851,  0.105,  12.73 , 1.9120, 2.000,  5.343),
"C_1"  : (0.706, 180.0   , 3.851,  0.105,  12.73 , 1.9120, 0.000,  5.343),
"N_3"  : (0.700, 106.7   , 3.660,  0.069,  13.407, 2.5438, 0.450,  6.899),
"N_R"  : (0.699, 120.0   , 3.660,  0.069,  13.407, 2.5438, 2.000,  6.899),
"N_2"  : (0.685, 111.3   , 3.660,  0.069,  13.407, 2.5438, 2.000,  6.899),
"N_1"  : (0.656, 180.0   , 3.660,  0.069,  13.407, 2.5438, 2.000,  6.899),
"O_3"  : (0.658, 104.51  , 3.500,  0.060,  14.085, 2.2998, 0.018,  8.741),
"O_3_z": (0.528, 145.5   , 3.500,  0.060,  14.085, 2.2998, 0.018,  8.741),
"O_R"  : (0.680, 110.3   , 3.500,  0.060,  14.085, 2.2998, 2.000,  8.741),
"O_2"  : (0.634, 120.0   , 3.500,  0.060,  14.085, 2.2998, 2.000,  8.741),
"O_1"  : (0.639, 180.0   , 3.500,  0.060,  14.085, 2.2998, 0.000,  8.741),
"O_3_f": (0.634, 109.4712, 3.500,  0.060,  14.085, 2.2998, 0.000,  8.741),
"O_4_f": (0.634,  90.0   , 3.500,  0.060,  14.085, 2.2998, 0.000,  8.741), # same as O_3_f but with 90.0 equil angle
"O_2_z": (0.528, 120.0   , 3.500,  0.060,  14.085, 2.2998, 0.000,  8.741),
"F_"   : (0.668, 180.0   , 3.364,  0.050,  14.762, 1.7350, 0.000, 10.874),
"Ne4+4": (0.920,  90.0   , 3.243,  0.042,  15.440, 0.1944, 0.000, 11.040),
"Na"   : (1.539, 180.0   , 2.983,  0.030,  12.0  , 1.0809, 0.000,  2.843),
"Na3f2": (1.623, 109.4712, 2.983,  0.030,  12.0  , 1.0809, 0.000,  2.843),
"Na4f2": (1.790,  90.0   , 2.983,  0.030,  12.0  , 1.0809, 0.000,  2.843),
"Mg3+2": (1.421, 109.4712, 3.021,  0.111,  12.0  , 1.7866, 0.000,  3.951),
"Mg6f3": (1.525,  90.0   , 3.021,  0.111,  12.0  , 1.7866, 0.000,  3.951),
"Al3"  : (1.244, 109.4712, 4.499,  0.505,  11.278, 1.7924, 0.000,  3.041),
"Al6+3": (1.220,  90.0   , 4.499,  0.505,  11.278, 1.7924, 0.000,  3.041),
"Al3f2": (1.280, 109.4712, 4.499,  0.505,  11.278, 1.7924, 0.000,  3.041),
"Si3"  : (1.117, 109.4712, 4.295,  0.402,  12.175, 2.3232, 1.225,  4.168),
"P_3+3": (1.101,  93.8   , 4.147,  0.305,  13.072, 2.8627, 2.400,  5.463),
"P_3+5": (1.056, 109.4712, 4.147,  0.305,  13.072, 2.8627, 2.400,  5.463),
"P_3+q": (1.056, 109.4712, 4.147,  0.305,  13.072, 2.8627, 2.400,  5.463),
"S_3+2": (1.064,  92.1   , 4.035,  0.274,  13.969, 2.7032, 0.484,  6.928),
"S_3"  : (1.064,  92.1   , 4.035,  0.274,  13.969, 2.7032, 0.484,  6.928),
"S_3+4": (1.049, 103.2   , 4.035,  0.274,  13.969, 2.7032, 0.484,  6.928),
"S_3+6": (1.027, 109.4712, 4.035,  0.274,  13.969, 2.7032, 0.484,  6.928),
"S_R"  : (1.077,  92.2   , 4.035,  0.274,  13.969, 2.7032, 1.250,  6.928),
"S_2"  : (0.854, 120.0   , 4.035,  0.274,  13.969, 2.7032, 1.250,  6.928),
"S_3_f": (0.854, 109.4712, 4.035,  0.274,  13.969, 2.7032, 0.484,  6.928),
"Cl"   : (1.044, 180.0   , 3.947,  0.227,  14.866, 2.3484, 0.000,  8.564),
"Cl_f" : (1.044,  90.0   , 3.947,  0.227,  14.866, 2.3484, 0.000,  8.564),
"Ar4+4": (1.032,  90.0   , 3.868,  0.185,  15.763, 0.2994, 0.000,  9.465),
"K"    : (1.953, 180.0   , 3.812,  0.035,  12.0  , 1.1645, 0.000,  2.421),
"K_3f2": (2.380, 109.4712, 3.812,  0.035,  12.0  , 1.1645, 0.000,  2.421),
"K_4f2": (2.010,  90.0   , 3.812,  0.035,  12.0  , 1.1645, 0.000,  2.421),
"Ca6+2": (1.761,  90.0   , 3.399,  0.238,  12.0  , 2.1414, 0.000,  3.231),
"Ca1f1": (1.560, 180.0   , 3.399,  0.238,  12.0  , 2.1414, 0.000,  3.231),
"Ca3f2": (1.705, 109.4712, 3.399,  0.238,  12.0  , 2.1414, 0.000,  3.231),
"Sc3+3": (1.513, 109.4712, 3.295,  0.019,  12.0  , 2.5924, 0.000,  3.395),
"Sc6+3": (1.440,  90.0   , 3.295,  0.019,  12.0  , 2.5924, 0.000,  3.395),
"Ti3+4": (1.412, 109.4712, 3.175,  0.017,  12.0  , 2.6595, 0.000,  3.470),
"Ti4+2": (1.380,  90.0   , 3.175,  0.017,  12.0  , 2.6595, 0.000,  3.470),
"Ti6+4": (1.412,  90.0   , 3.175,  0.017,  12.0  , 2.6595, 0.000,  3.470),
"Ti8f4": (1.460, 109.4712, 3.175,  0.017,  12.0  , 2.6595, 0.000,  3.470),
"V_3+5": (1.402, 109.4712, 3.144,  0.016,  12.0  , 2.6789, 0.000,  3.650),
"V_4+2": (1.18 ,  90.0   , 3.144,  0.016,  12.0  , 2.6789, 0.000,  3.650),
"V_6+3": (1.30 ,  90.0   , 3.144,  0.016,  12.0  , 2.6789, 0.000,  3.650),
"V_3f2": (1.120, 109.4712, 3.144,  0.016,  12.0  , 2.6789, 0.000,  3.650),
"Cr6+3": (1.345,  90.0   , 3.023,  0.015,  12.0  , 2.4631, 0.000,  3.415),
"Cr4+2": (1.10 ,  90.0   , 3.023,  0.015,  12.0  , 2.4631, 0.000,  3.415),
"Cr6f3": (1.28 ,  90.0   , 3.023,  0.015,  12.0  , 2.4631, 0.000,  3.415),
"Mn6+2": (1.382,  90.0   , 2.961,  0.013,  12.0  , 2.4301, 0.000,  3.325),
"Mn6+3": (1.34 ,  90.0   , 2.961,  0.013,  12.0  , 2.4301, 0.000,  3.325),
"Mn4+2": (1.26 ,  90.0   , 2.961,  0.013,  12.0  , 2.4301, 0.000,  3.325),
"Mn1f1": (1.380, 180.0   , 2.961,  0.013,  12.0  , 2.4301, 0.000,  3.325),
"Mn3f2": (1.180, 109.4712, 2.961,  0.013,  12.0  , 2.4301, 0.000,  3.325),
"Mn8f4": (1.520, 109.4712, 2.961,  0.013,  12.0  , 2.4301, 0.000,  3.325),
"Fe3+2": (1.270, 109.4712, 2.912,  0.013,  12.0  , 2.4301, 0.000,  3.760),
"Fe6+2": (1.335,  90.0   , 2.912,  0.013,  12.0  , 2.4301, 0.000,  3.760),
"Fe6+3": (1.32 ,  90.0   , 2.912,  0.013,  12.0  , 2.4301, 0.000,  3.760),
"Fe4+2": (1.10 ,  90.0   , 2.912,  0.013,  12.0  , 2.4301, 0.000,  3.760),
"Fe1f1": (1.380, 180.0   , 2.912,  0.013,  12.0  , 2.4301, 0.000,  3.760),
"Co6+2": (1.241,  90.0   , 2.872,  0.014,  12.0  , 2.4301, 0.000,  4.105),
"Co3+2": (1.24 , 109.4712, 2.872,  0.014,  12.0  , 2.4301, 0.000,  4.105),
"Co4+2": (1.16 ,  90.0   , 2.872,  0.014,  12.0  , 2.4301, 0.000,  4.105),
"Co1f1": (1.280, 180.0   , 2.872,  0.014,  12.0  , 2.4301, 0.000,  4.105),
"Ni4+2": (1.164,  90.0   , 2.834,  0.015,  12.0  , 2.4301, 0.000,  4.465),
"Cu3+1": (1.302, 109.4712, 3.495,  0.005,  12.0  , 1.7565, 0.000,  3.729),
"Cu4+2": (1.28 ,  90.0   , 3.495,  0.005,  12.0  , 1.7565, 0.000,  3.729),
"Cu1f1": (1.240, 180.0   , 3.495,  0.005,  12.0  , 1.7565, 0.000,  3.729),
"Cu2f2": (1.110, 120.0   , 3.495,  0.005,  12.0  , 1.7565, 0.000,  3.729),
"Cu3f2": (1.190, 109.4712, 3.495,  0.005,  12.0  , 1.7565, 0.000,  3.729),
"Zn3+2": (1.193, 109.4712, 2.763,  0.124,  12.0  , 1.3084, 0.000,  5.106),
"Zn4+2": (1.34 ,  90.0   , 2.763,  0.124,  12.0  , 1.3084, 0.000,  5.106),
"Zn3f2": (1.24 , 109.4712, 2.763,  0.124,  12.0  , 1.3084, 0.000,  5.106),
"Zn1f1": (1.300, 180.0   , 2.763,  0.124,  12.0  , 1.3084, 0.000,  5.106),
"Zn2f2": (1.300, 120.0   , 2.763,  0.124,  12.0  , 1.3084, 0.000,  5.106),
"Ga3+3": (1.260, 109.4712, 4.383,  0.415,  11.0  , 1.8206, 0.000,  2.999),
"Ga3f2": (1.150, 109.4712, 4.383,  0.415,  11.0  , 1.8206, 0.000,  2.999),
"Ga6f3": (1.480, 90.0    , 4.383,  0.415,  11.0  , 1.8206, 0.000,  2.999),
"Ge3"  : (1.197, 109.4712, 4.280,  0.379,  12.0  , 2.7888, 0.701,  4.051),
"As3+3": (1.211,  92.1   , 4.230,  0.309,  13.0  , 2.8640, 1.500,  5.188),
"Se3+2": (1.190,  90.6   , 4.205,  0.291,  14.0  , 2.7645, 0.335,  6.428),
"Br"   : (1.192, 180.0   , 4.189,  0.251,  15.0  , 2.5186, 0.000,  7.790),
"Kr4+4": (1.147,  90.0   , 4.141,  0.220,  16.0  , 0.4520, 0.000,  8.505),
"Rb"   : (2.260, 180.0   , 4.114,  0.040,  12.0  , 1.5922, 0.000,  2.331),
"Sr6+2": (2.052,  90.0   , 3.641,  0.235,  12.0  , 2.4486, 0.000,  3.024),
"Sr8f4": (1.820, 109.4712, 3.641,  0.235,  12.0  , 2.4486, 0.000,  3.024),
"Y_3+3": (1.698, 109.4712, 3.345,  0.072,  12.0  , 3.2573, 0.000,  3.830),
"Y_6f3": (1.600,  90.0   , 3.345,  0.072,  12.0  , 3.2573, 0.000,  3.830),
"Y_8f4": (1.680, 109.4712, 3.345,  0.072,  12.0  , 3.2573, 0.000,  3.830),
"Zr3+4": (1.564, 109.4712, 3.124,  0.069,  12.0  , 3.6675, 0.000,  3.400),
"Zr8f4": (1.680, 109.4712, 3.124,  0.069,  12.0  , 3.6675, 0.000,  3.400),
"Nb3+5": (1.473, 109.4712, 3.165,  0.059,  12.0  , 3.6179, 0.000,  3.550),
"Nb8f4": (1.370, 109.4712, 3.165,  0.059,  12.0  , 3.6179, 0.000,  3.550),
"Mo6+6": (1.467,  90.0000, 3.052,  0.056,  12.0  , 3.4021, 0.000,  3.465),
"Mo3+6": (1.484, 109.4712, 3.052,  0.056,  12.0  , 3.4021, 0.000,  3.465),
"Mo3f2": (1.240, 109.4712, 3.052,  0.056,  12.0  , 3.4021, 0.000,  3.465),
"Mo4f2": (1.400,  90.0   , 3.052,  0.056,  12.0  , 3.4021, 0.000,  3.465),
"Mo8f4": (1.280, 109.4712, 3.052,  0.056,  12.0  , 3.4021, 0.000,  3.465),
"Tc6+5": (1.322,  90.0000, 2.998,  0.048,  12.0  , 3.4021, 0.000,  3.290),
"Ru6+2": (1.478,  90.0000, 2.963,  0.056,  12.0  , 3.4021, 0.000,  3.575),
"Ru4f2": (1.320,  90.0000, 2.963,  0.056,  12.0  , 3.4021, 0.000,  3.575),
"Rh6+3": (1.332,  90.0000, 2.929,  0.053,  12.0  , 3.5081, 0.000,  3.975),
"Pd4+2": (1.338,  90.0000, 2.899,  0.048,  12.0  , 3.2077, 0.000,  4.320),
"Pd6f3": (1.190,  90.0000, 2.899,  0.048,  12.0  , 3.2077, 0.000,  4.320),
"Ag1+1": (1.386, 180.0000, 3.148,  0.036,  12.0  , 1.9557, 0.200,  4.436),
"Ag1f1": (1.220, 180.0000, 3.148,  0.036,  12.0  , 1.9557, 0.200,  4.436),
"Ag2f2": (1.340, 120.0000, 3.148,  0.036,  12.0  , 1.9557, 0.200,  4.436),
"Ag3f2": (1.480, 109.4712, 3.148,  0.036,  12.0  , 1.9557, 0.200,  4.436),
"Ag4f2": (1.510,  90.0000, 3.148,  0.036,  12.0  , 1.9557, 0.200,  4.436),
"Cd3+2": (1.403, 109.4712, 2.848,  0.228,  12.0  , 1.6525, 0.000,  5.034),
"Cd1f1": (1.400, 180.0000, 2.848,  0.228,  12.0  , 1.6525, 0.000,  5.034),
"Cd3f2": (1.290, 109.4712, 2.848,  0.228,  12.0  , 1.6525, 0.000,  5.034),
"Cd4f2": (1.460,  90.0000, 2.848,  0.228,  12.0  , 1.6525, 0.000,  5.034),
"Cd8f4": (1.640, 109.4712, 2.848,  0.228,  12.0  , 1.6525, 0.000,  5.034),
"In3+3": (1.459, 109.4712, 4.463,  0.599,  11.0  , 2.0704, 0.000,  2.997),
"In3f2": (1.330, 109.4712, 4.463,  0.599,  11.0  , 2.0704, 0.000,  2.997),
"In6f3": (1.530,  90.0000, 4.463,  0.599,  11.0  , 2.0704, 0.000,  2.997),
"In8f4": (1.530, 109.4712, 4.463,  0.599,  11.0  , 2.0704, 0.000,  2.997),
"Sn3"  : (1.398, 109.4712, 4.392,  0.567,  12.0  , 2.9608, 0.199,  3.987),
"Sb3+3": (1.407,  91.6000, 4.420,  0.449,  13.0  , 2.7042, 1.100,  4.899),
"Te3+2": (1.386,  90.2500, 4.470,  0.398,  14.0  , 2.8821, 0.300,  5.816),
"I_"   : (1.382, 180.0000, 4.500,  0.339,  15.0  , 2.6537, 0.000,  6.822),
"Xe4+4": (1.267,  90.0000, 4.404,  0.332,  12.0  , 0.5560, 0.000,  7.595),
"Cs"   : (2.570, 180.0000, 4.517,  0.045,  12.0  , 1.5728, 0.000,  2.183),
"Ba6+2": (2.277,  90.0000, 3.703,  0.364,  12.0  , 2.7266, 0.000,  2.814),
"Ba3f2": (2.040, 109.4712, 3.703,  0.364,  12.0  , 2.7266, 0.000,  2.814),
"La3+3": (1.943, 109.4712, 3.522,  0.017,  12.0  , 3.3049, 0.000,  2.8355),
"La8f4": (1.660, 109.4712, 3.522,  0.017,  12.0  , 3.3049, 0.000,  2.8355),
"Ce6+3": (1.841,  90.0000, 3.556,  0.013,  12.0  , 3.3049, 0.000,  2.774),
"Ce8f4": (1.760, 109.4712, 3.556,  0.013,  12.0  , 3.3049, 0.000,  2.774),
"Pr6+3": (1.823,  90.0000, 3.606,  0.010,  12.0  , 3.3049, 0.000,  2.858),
"Pr8f4": (1.830, 109.4712, 3.606,  0.010,  12.0  , 3.3049, 0.000,  2.858),
"Nd6+3": (1.816,  90.0000, 3.575,  0.010,  12.0  , 3.3049, 0.000,  2.8685),
"Nd8f4": (1.780, 109.4712, 3.575,  0.010,  12.0  , 3.3049, 0.000,  2.8685),
"Pm6+3": (1.801,  90.0000, 3.547,  0.009,  12.0  , 3.3049, 0.000,  2.881),
"Sm6+3": (1.780,  90.0000, 3.520,  0.008,  12.0  , 3.3049, 0.000,  2.9115),
"Sm8f4": (1.780, 109.4712, 3.520,  0.008,  12.0  , 3.3049, 0.000,  2.9115),
"Eu6+3": (1.771,  90.0000, 3.493,  0.008,  12.0  , 3.3049, 0.000,  2.8785),
"Eu6f3": (1.600,  90.0000, 3.493,  0.008,  12.0  , 3.3049, 0.000,  2.8785),
"Eu8f4": (1.740, 109.4712, 3.493,  0.008,  12.0  , 3.3049, 0.000,  2.8785),
"Gd6+3": (1.735,  90.0000, 3.368,  0.009,  12.0  , 3.3049, 0.000,  3.1665),
"Gd6f3": (1.550,  90.0000, 3.368,  0.009,  12.0  , 3.3049, 0.000,  3.1665),
"Gd8f4": (1.700, 109.4712, 3.368,  0.009,  12.0  , 3.3049, 0.000,  3.1665),
"Tb6+3": (1.732,  90.0000, 3.451,  0.007,  12.0  , 3.3049, 0.000,  3.018),
"Tb8f4": (1.640, 109.4712, 3.451,  0.007,  12.0  , 3.3049, 0.000,  3.018),
"Dy6+3": (1.710,  90.0000, 3.428,  0.007,  12.0  , 3.3049, 0.000,  3.0555),
"Dy6f3": (1.580,  90.0000, 3.428,  0.007,  12.0  , 3.3049, 0.000,  3.0555),
"Dy8f4": (1.700, 109.4712, 3.428,  0.007,  12.0  , 3.3049, 0.000,  3.0555),
"Ho6+3": (1.696,  90.0000, 3.409,  0.007,  12.0  , 3.4157, 0.000,  3.127),
"Ho8f4": (1.700, 109.4712, 3.409,  0.007,  12.0  , 3.4157, 0.000,  3.127),
"Er6+3": (1.673,  90.0000, 3.391,  0.007,  12.0  , 3.3049, 0.000,  3.1865),
"Er8f4": (1.640, 109.4712, 3.391,  0.007,  12.0  , 3.3049, 0.000,  3.1865),
"Tm6+3": (1.660,  90.0000, 3.374,  0.006,  12.0  , 3.3049, 0.000,  3.2514),
"Tm8f4": (1.670, 109.4712, 3.374,  0.006,  12.0  , 3.3049, 0.000,  3.2514),
"Yb6+3": (1.637,  90.0000, 3.355,  0.228,  12.0  , 2.6177, 0.000,  3.2889),
"Yb6f3": (1.450,  90.0000, 3.355,  0.228,  12.0  , 2.6177, 0.000,  3.2889),
"Yb8f4": (1.620, 109.4712, 3.355,  0.228,  12.0  , 2.6177, 0.000,  3.2889),
"Lu6+3": (1.671,  90.0000, 3.640,  0.041,  12.0  , 3.2709, 0.000,  2.9629),
"Lu1f1": (1.650, 180.0000, 3.640,  0.041,  12.0  , 3.2709, 0.000,  2.9629),
"Lu8f4": (1.660, 109.4712, 3.640,  0.041,  12.0  , 3.2709, 0.000,  2.9629),
"Hf3+4": (1.611, 109.4712, 3.141,  0.072,  12.0  , 3.9212, 0.000,  3.7000),
"Hf8f4": (1.460, 109.4712, 3.141,  0.072,  12.0  , 3.9212, 0.000,  3.7000),
"Ta3+5": (1.511, 109.4712, 3.170,  0.081,  12.0  , 4.0748, 0.000,  5.1000),
"W_6+6": (1.392,  90.0000, 3.069,  0.067,  12.0  , 3.6937, 0.000,  4.6300),
"W_3+4": (1.526, 109.4712, 3.069,  0.067,  12.0  , 3.6937, 0.000,  4.6300),
"W_3+6": (1.380, 109.4712, 3.069,  0.067,  12.0  , 3.6937, 0.000,  4.6300),
"W_3f4": (1.160, 109.4712, 3.069,  0.067,  12.0  , 3.6937, 0.000,  4.6300),
"W_4f2": (1.345,  90.0000, 3.069,  0.067,  12.0  , 3.6937, 0.000,  4.6300),
"W_8f4": (1.270, 109.4712, 3.069,  0.067,  12.0  , 3.6937, 0.000,  4.6300),
"Re6+5": (1.372,  90.0000, 2.954,  0.066,  12.0  , 3.6937, 0.000,  3.9600),
"Re3+7": (1.314, 109.4712, 2.954,  0.066,  12.0  , 3.6937, 0.000,  3.9600),
"Re6f3": (1.230,  90.0000, 2.954,  0.066,  12.0  , 3.6937, 0.000,  3.9600),
"Os4f2": (1.240,  90.0000, 3.120,  0.037,  12.0  , 3.6937, 0.000,  5.1400),
"Os6+6": (1.372,  90.0000, 3.120,  0.037,  12.0  , 3.6937, 0.000,  5.1400),
"Ir6+3": (1.371,  90.0000, 2.840,  0.073,  12.0  , 3.7307, 0.000,  5.0000),
"Pt4+2": (1.364,  90.0000, 2.754,  0.080,  12.0  , 3.3817, 0.000,  4.7900),
"Pt4f2": (1.125,  90.0000, 2.754,  0.080,  12.0  , 3.3817, 0.000,  4.7900),
"Au4+3": (1.262,  90.0000, 3.293,  0.039,  12.0  , 2.6255, 0.000,  4.8940),
"Au1f1": (1.110, 180.0000, 3.293,  0.039,  12.0  , 2.6255, 0.000,  4.8940),
"Hg1+2": (1.340, 180.0000, 2.705,  0.385,  12.0  , 1.7497, 0.000,  6.2700),
"Hg3f2": (1.248, 109.4712, 2.705,  0.385,  12.0  , 1.7497, 0.000,  6.2700),
"Tl3+3": (1.518, 120.0000, 4.347,  0.680,  11.0  , 2.0685, 0.000,  3.2000),
"Pb3"  : (1.459, 109.4712, 4.297,  0.663,  12.0  , 2.8461, 0.100,  3.9000),
"Pb4f2": (1.670,  90.0000, 4.297,  0.663,  12.0  , 2.8461, 0.100,  3.9000),
"Bi3+3": (1.512,  90.0000, 4.370,  0.518,  13.0  , 2.4700, 1.000,  4.6900),
"Po3+2": (1.500,  90.0000, 4.709,  0.325,  14.0  , 2.3329, 0.300,  4.2100),
"At"   : (1.545, 180.0000, 4.750,  0.284,  15.0  , 2.2357, 0.000,  4.7500),
"Rn4+4": (1.420,  90.0000, 4.765,  0.248,  16.0  , 0.5832, 0.000,  5.3700),
"Fr"   : (2.880, 180.0000, 4.900,  0.050,  12.0  , 1.8469, 0.000,  2.0000),
"Ra6+2": (2.512,  90.0000, 3.677,  0.404,  12.0  , 2.9161, 0.000,  2.8430),
"Ac6+3": (1.983,  90.0000, 3.478,  0.033,  12.0  , 3.8882, 0.000,  2.8350),
"Th6+4": (1.721,  90.0000, 3.396,  0.026,  12.0  , 4.2021, 0.000,  3.1750),
"Pa6+4": (1.711,  90.0000, 3.424,  0.022,  12.0  , 3.8882, 0.000,  2.9850),
"U_6+4": (1.684,  90.0000, 3.395,  0.022,  12.0  , 3.8882, 0.000,  3.3410),
"U_6f3": (1.650,  90.0000, 3.395,  0.022,  12.0  , 3.8882, 0.000,  3.3410),
"U_8f4": (1.730, 109.4712, 3.395,  0.022,  12.0  , 3.8882, 0.000,  3.3410),
"Np6+4": (1.666,  90.0000, 3.424,  0.019,  12.0  , 3.8882, 0.000,  3.5490),
"Pu6+4": (1.657,  90.0000, 3.424,  0.016,  12.0  , 3.8882, 0.000,  3.2430),
"Am6+4": (1.660,  90.0000, 3.381,  0.014,  12.0  , 3.8882, 0.000,  2.9895),
"Cm6+3": (1.801,  90.0000, 3.326,  0.013,  12.0  , 3.8882, 0.000,  2.8315),
"Bk6+3": (1.761,  90.0000, 3.339,  0.013,  12.0  , 3.8882, 0.000,  3.1935),
"Cf6+3": (1.750,  90.0000, 3.313,  0.013,  12.0  , 3.8882, 0.000,  3.1970),
"Es6+3": (1.724,  90.0000, 3.299,  0.012,  12.0  , 3.8882, 0.000,  3.3330),
"Fm6+3": (1.712,  90.0000, 3.286,  0.012,  12.0  , 3.8882, 0.000,  3.4000),
"Md6+3": (1.689,  90.0000, 3.274,  0.011,  12.0  , 3.8882, 0.000,  3.4700),
"No6+3": (1.679,  90.0000, 3.248,  0.011,  12.0  , 3.8882, 0.000,  3.4750),
"Lr6+3": (1.698,  90.0000, 3.236,  0.011,  12.0  , 3.8882, 0.000,  3.5000),
### Special O-types for using alternate bond orders
"O_2_M": (0.634, 120.00, 3.500, 0.060, 14.085, 2.3000, 2.000, 8.7410), # carboxyllic oxygen bonded to metal
"O_3_M": (0.658, 104.51, 3.500, 0.060, 14.085, 2.3000, 0.018, 8.7410)  # this should be used for O in coordinated solvent
}

# without MIL-53 type nodes
UFF4MOF_bond_orders_0 = {
	("Ti4+2", "Ti4+2") : 0.25,
	("V_4+2", "V_4+2") : 3.00,
	("Cr4+2", "Cr4+2") : 4.00,
	("Mn4+2", "Mn4+2") : 0.25,
	("Fe4+2", "Fe4+2") : 0.25,
	("Co4+2", "Co4+2") : 0.25,
	("Cu4+2", "Cu4+2") : 0.25,
	("Zn4+2", "Zn4+2") : 0.25,
	("Al6+3", "O_2_M") : 0.50,
	("Sc6+3", "O_2_M") : 0.50,
	("Ti4+2", "O_2_M") : 0.50,
	("V_4+2", "O_2_M") : 0.50,
	("V_6+3", "O_2_M") : 0.50,
	("Cr4+2", "O_2_M") : 0.50,
	("Cr6f3", "O_2_M") : 0.50,
	("Co6+2", "O_2_M") : 0.50,
	("Mn6+3", "O_2_M") : 0.50,
	("Mg6f3", "O_2_M") : 0.50, # this may need to be 1/2
	("Mn4+2", "O_2_M") : 0.50,
	("Fe6+3", "O_2_M") : 0.50,
	("Fe4+2", "O_2_M") : 0.50,
	("Co3+2", "O_2_M") : 0.50,
	("Co4+2", "O_2_M") : 0.50,
	("Cu4+2", "O_2_M") : 0.50,
	("Zn4+2", "O_2_M") : 0.50,
	("Zn3f2", "O_2_M") : 0.50,
	("Zr8f4", "O_2_M") : 0.50,
	("Al6+3", "O_2_M") : 0.50,
	("Sc6+3", "O_2_z") : 1.00,
	("V_6+3", "O_2_z") : 1.00,
	("Al6+3", "O_2_z") : 1.00,
	("Cr6f3", "O_2_z") : 1.00,
	("Mg6f3", "O_2_z") : 1.00,
	("Fe6+3", "O_2_z") : 1.00,
	("Mn6+3", "O_2_z") : 1.00,
	("Zr8f4", "O_3_M") : 0.50,
	("Al6+3", "O_3_M") : 0.50,
	("Fe6+3", "O_3_M") : 0.50,
	("Cr6f3", "O_3_M") : 0.50,
	("Zn3f2", "O_3_f") : 0.50,
	("Zr8f4", "O_3_f") : 0.50,
	("Co6+2", "O_4_f") : 0.25,
	("Mn6+2", "Cl_f" ) : 0.25,
	("Mn6+2", "N_R"  ) : 0.50,
	'S': 1.00,
	'A': 1.50,
	'D': 2.00,
	'T': 3.00
}