myList = [1, 2, 3]
myDict = {'Name': 'Phuong', 'age':'20'}
for num in myList:
    print(num)
for key, value in myDict.items():
    print(key, value)
mgs = ''
while mgs != 'quit':
    mgs = input("Please give me an input: ")
    print(mgs)