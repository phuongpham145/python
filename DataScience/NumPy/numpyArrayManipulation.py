import numpy as np
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(a)
print(a.shape)
b = a.reshape(4, 2)
print(b)
c = a.reshape(2, 2, 2)
print(c)
np_cube = np.random.random((2, 2, 2))
print(np_cube)
print(np_cube.shape)
tmp = np_cube.flatten()
print(tmp)
print(tmp.shape)
a = np.array([
    [1, 2],
    [4, 5]
])
print(a)
print(a.shape)
b = np.expand_dims(a, axis=0)
print(b)
print(b.shape)
c = np.expand_dims(a, axis=2)
print(c)
print(c.shape)
np_cube = np.random.random((1, 2, 2, 1))
print(np_cube)
result = np.squeeze(np_cube, axis = 0)
print(result)
print(result.shape)
np_matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(np_matrix)
print(np_matrix.shape)
print(np_matrix.T)
print(np_matrix.T.shape)
print(np.transpose(np_matrix))
print(np.transpose(np_matrix).shape)