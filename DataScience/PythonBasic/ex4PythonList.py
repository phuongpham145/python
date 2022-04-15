list = [1, 2, 3, 'Hello', True, 3.23, False, 100]
print(list)
print(len(list))
print(list[3])
print(type(list[-3]))
print(list[len(list)-1])
list1 = [1, 2, ('tuples', 3, 3.4), [3, 4, 5], (True, False), 'end']
print(list1)
print(type(list1[2]))
print(list1[-2][1])
print(list1[3])
print(list1[:3])
print(list1[3:])
print(list1[2:4])
list1.extend(['hello', 'end'])
print(list1)
print(len(list1))
list1.append(['goodbye', 'goodbye You'])
print(list1)
print(len(list1))
list[-1] = '1111'
print(list)
del(list[-1])
print(list)
name = 'Pham Van Phuong'
name = name.split(" ")
print(name)
print(len(name))
print(name[-1])
#Copy
a = [1, 2, 3]
b = a
print(a)
print(b)
b[0] = 999
print(a)
print(b)
a[-1] = 888
print(a)
print(b)
#Clone
a = [4, 5, 6]
b = a[:]
print(a)
print(b)
b[0] = 999
print(a)
print(b)
a[-1] = 888
print(a)
print(b)