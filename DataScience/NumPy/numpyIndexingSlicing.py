import numpy as np
np_matrix = np.array([
    [1, 2, 3],
    [9, 7, 10]
])
print(np_matrix)
print(np_matrix[0, :2])
print(np_matrix[:, 0])
print(np_matrix[-1])
print(np_matrix[-1, :2])
print(np_matrix[:1, :2])
np_matrixp = np.random.random((4, 6))
print(np_matrixp)
print('result1')
print(np_matrixp[0:1][-1])
print('result2')
print(np_matrixp[0:1][-1][1:3])