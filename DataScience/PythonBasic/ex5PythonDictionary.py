dic = {'key1' : 2, 'key2' : "hello", 'key3' : ('tuples', 1, 2), (0, 1): True}
print(dic)
print(dic['key3'])
dic = {'key1' : 3, 'key2' : 4, 'key1': 'hello'}
print(dic)
print(dic.keys())
print(type(dic.keys()))
print(dic.values())
print(type(dic.values()))
dic['key3'] = "Pham Phuong"
print(dic)  
del(dic['key2'])
print(dic)
print(('key1') in dic)
