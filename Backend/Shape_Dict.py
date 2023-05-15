import numpy as np

shape_options = {
    'Circle': {
        'points': [[ (0.0627905195293, -0.998026728428), (0.187381314586, -0.982287250729), (0.309016994375, -0.951056516295), (0.425779291565, -0.904827052466), (0.535826794979, -0.844327925502), (0.637423989749, -0.770513242776), (0.728968627421, -0.684547105929), (0.809016994375, -0.587785252292), (0.876306680044, -0.481753674102), (0.929776485888, -0.368124552685), (0.968583161129, -0.248689887165), (0.992114701314, -0.125333233564), (1.0, 0.0), (0.992114701314, 0.125333233564), (0.968583161129, 0.248689887165), (0.929776485888, 0.368124552685), (0.876306680044, 0.481753674102), (0.809016994375, 0.587785252292), (0.728968627421, 0.684547105929), (0.637423989749, 0.770513242776), (0.535826794979, 0.844327925502), (0.425779291565, 0.904827052466), (0.309016994375, 0.951056516295), (0.187381314586, 0.982287250729), (0.0627905195293, 0.998026728428), (-0.0627905195293, 0.998026728428), (-0.187381314586, 0.982287250729), (-0.309016994375, 0.951056516295), (-0.425779291565, 0.904827052466), (-0.535826794979, 0.844327925502), (-0.637423989749, 0.770513242776), (-0.728968627421, 0.684547105929), (-0.809016994375, 0.587785252292), (-0.876306680044, 0.481753674102), (-0.929776485888, 0.368124552685), (-0.968583161129, 0.248689887165), (-0.992114701314, 0.125333233564), (-1.0, -1.20980294964e-15), (-0.992114701314, -0.125333233564), (-0.968583161129, -0.248689887165), (-0.929776485888, -0.368124552685), (-0.876306680044, -0.481753674102), (-0.809016994375, -0.587785252292), (-0.728968627421, -0.684547105929), (-0.637423989749, -0.770513242776), (-0.535826794979, -0.844327925502), (-0.425779291565, -0.904827052466), (-0.309016994375, -0.951056516295), (-0.187381314586, -0.982287250729), (-0.0627905195293, -0.998026728428), (0.0627905195293, -0.998026728428)]]
    },
    'Triangle': {
        'points': [[(3, 0), (0, 3/np.sqrt(3)), (-3, 0), (3, 0)]]
    },
    'Hexagon': {
        'points': [[(1/2, -np.sqrt(3)/2), (1, 0), (1/2, np.sqrt(3)/2), (-1/2, np.sqrt(3)/2), (-1, 0), (-1/2, -np.sqrt(3)/2), (1/2, -np.sqrt(3)/2)]]
    },
    'Star': {
        'points': [[(23.78,10.12), (21.42,16.86), (18.88,10.16), (25.06,14.38), (18.06,14.44), (23.78,10.12)]]
    },
    'Heart': {
        'points': [[(235.701, -410.701), (57.401, -232.401), (44.38225, -216.5744375), (34.851, -198.7885), (28.99475, -179.4838125), (27.001, -159.101), (28.979125, -138.71975), (34.801, -119.426), (44.297875, -101.66975), (57.301, -85.901), (73.0681875, -72.9400625), (90.8135, -63.4385), (110.0775625, -57.5931875), (130.401, -55.601), (150.7994375, -57.59475), (170.1385, -63.451), (187.9588125, -72.98225), (203.801, -86.001), (226.401, -108.601), (230.876, -111.58225), (235.951, -112.576), (241.026, -111.58225), (245.501, -108.601), (267.901, -86.201), (283.741625, -73.18225), (301.551, -63.651), (320.860375, -57.79475), (341.201, -55.801), (361.526, -57.7931875), (380.801, -63.6385), (398.576, -73.1400625), (414.401, -86.101), (427.404125, -101.9275625), (436.901, -119.7135), (442.722875, -139.0181875), (444.701, -159.401), (442.7650625, -179.7838125), (436.9385, -199.0885), (427.4181875, -216.8744375), (414.401, -232.701), (235.701, -410.701)]]
    }
}