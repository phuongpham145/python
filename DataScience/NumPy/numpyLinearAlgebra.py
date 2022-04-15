import numpy as np
from numpy import linalg
a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
print(a * b)
print(np.inner(a, b))
a = np.array([
    [1, 2, 3],
    [3, 1, 0]
])
b = np.array([
    [2, 1, 3],
    [1, 3, 4],
    [3, 1, 0]
])
print(a.dot(b))
A = np.array([
    [2, 0, 6],
    [1, -1, 2]
])
B = np.array([
    [8, -3, 2],
    [4, 1, -5]
])
print(np.tensordot(A, B))
#Tong can binh phuong cua cac gia tri vector
A = np.array([1, 2, 3, 2, 3, 4])
print(linalg.norm(A))
B = np.array([6, 20, 10, -4])
print(linalg.norm(B, ord=1))
A = np.array([
    [1, 3],
    [1, 0],
    [1, 2]
])
B = np.array([
    [0, 0],
    [7, 5], 
    [2, 1]
])
print(np.add(A, B))
print(np.subtract(A, B))