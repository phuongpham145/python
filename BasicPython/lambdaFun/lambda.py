phuongpham = lambda so : so + 69
def pham(so):
    return so + 60
print(pham(11))

#Sort
coordinate2D = [(6, 9), (5, 9), (-1, 3), (2, 10)]
print(sorted(coordinate2D))
print(sorted(coordinate2D, key = lambda point: point[1]))
numberList = [5, 3, -2, 4, 1, -1, -3, 4, 5]
print(sorted(numberList, key = lambda x : abs(x)))

#Map
listKeywords = ["Pham", "Van", "Phuong", "Xin", "Chao"]
print(list(map(lambda x :x.title(), listKeywords)))

#filter
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(filter(lambda x : x%2!=0, numberList)))

#reduce
from functools import reduce
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(reduce(lambda a, b : a + b, sequence))
print(reduce(lambda a, b : a if  a > b else b, sequence))