import numpy as np
a = np.array([1, 2, 3, 4, 5, 3, 8])
print(a)
print(a.ndim) # So chieu cua mang
print(a[0]) # Lay phan tu dau tien cua mang den thu 3
print(a[0:3]) # Lay phan tu dau tien den thu 3
print(a[0:3:2]) # Lay phan tu dau tien den thu 3, chia het cho 2
print(a[::-1]) # Lay phan tu cuoi cung den dau tien
print(a[::-2]) # Lay phan tu cuoi cung den dau tien, chia het cho 2
print(a[::-3]) # Lay phan tu cuoi cung den dau tien, chia het cho 3
print(len(a))
b = np.array([[1, 2, 3, 4, 5, 3, 8], [9, 4, 3, 4, 5, 3, 8]])
print(b)
print(b.ndim)
print(b[0])
print(b[0][0])
print(b[0][0:3])
print(b[0][0:3:2])
print(b[0][::-1])
print(b[0][::-2])
print(b.shape)
c = np.arange(20)
print(c)