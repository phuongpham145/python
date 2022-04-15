import numpy as np
np_vector = np.array([1, 2, 3])
print(np_vector)
np_vector = np_vector + 3
print(np_vector)
np_vector = np_vector +np.array([3, 3, 3])
print(np_vector)
np_vector = np_vector - 3
print(np_vector)
np_matrix = np.array([
    [4, 5, 6],
    [7, 8, 9]
])
print(np_matrix)
np_matrix = np_matrix*2
print(np_matrix)
np_vector = np.arange(0, 20, 3)
print(np_vector)
np_vector *= 3
print(np_vector)
np_matrix = np.ones((3, 5))
print(np_matrix)
np_matrix *= 3
print(np_matrix)
a = np.ones((3, 5))
print(a)
b = np.arange(5)
print(b)
print(a + b)
a = np.arange(5).reshape(5, 1)
print(a)
b = np.arange(5)
print(b)
c = a + b
print(c)
print(c.shape)
a = np.array([
    [1, 2, 3],
    [2, 3, 4]
])
b = np.arange(3)
print(a)
print(b)
print(a + b)
a = np.array([
    [1, 2, 3],
    [2, 3, 4]
])
c = np.array([
    [1],
    [9]
])
print(a)
print(c)
print( a + c)