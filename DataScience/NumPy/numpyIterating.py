import numpy as np
np_vector = np.random.random(5, )
print(np_vector)
for x in np.nditer(np_vector):
    print(x)
np_matrix = np.random.random((2, 3))
print(np_matrix)
for x in np.nditer(np_matrix):
    print(x)
np_cube = np.random.random((2, 2, 2))
print(np_cube)
for x in np.nditer(np_cube):
    print(x)
np_matrix = np.random.random((2, 3))
print(np_matrix)
for x in np.nditer(np_matrix, flags = ['external_loop'], order = 'F'):
    print(x)
for x in np.nditer(np_matrix, flags = ['external_loop'], order = 'C'):
    print(x)