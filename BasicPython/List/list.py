from typing import final


list1 = ["banana", "apple", "orange", "cherry"]
print(len(list1))
print(list1[2])
print(list1.index("apple"))
print(list1.count("banana"))
print(list1)
for item in list1:
    print(item)
presidents = ["Washington", "Adams", "Jeffeerson", "Madison", "Monroe", "Adams", "Jackson"]
for index, president in enumerate(presidents, start=1):
    print(f"President #{index}: {president}")

# Slicing
print(presidents[1:3])
print(presidents[-1])
print(presidents[::2])
print(presidents[::-1])

#List operations & Useful method
myList = [1, 2, '3', True]
print(myList*2 + [100, "Pham"])
myList.append(100)
print(myList)
myList.extend([100, "Pham"])
print(myList)
myList.insert(3, 4)
print(myList)

#Remove
myList.pop()
myList.pop(1)
print(myList)
myList.remove(4)
print(myList)

#sort
watashinoList = [1, 4, 5, 6, 2, 8, 0]
watashinoList.reverse()
watashinoList.sort(reverse=True)
print(sorted(watashinoList))
print(watashinoList)
print(max(watashinoList))
print(min(watashinoList))
print(sum(watashinoList))

#List Comperhernet
word = "Hello Word"
print([char for char in word])
evenNumbers = [i for i in range(0, 100) if i%2 ==0]
print(evenNumbers)
transactions = [100, 200, 300, 150, 80]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07
def getPrice(bill):
    return bill*(1 + TAX_RATE + SERVICE_CHARGE)
finalPrice = [ getPrice(bill) for bill in transactions]
print(finalPrice)

#Advanced fnction
myStrings = "Welcome to Vietnam"
listOfChars = list(myStrings)
print(listOfChars)
wizards = ['Harry Potter', 'Ron', 'Hermione']
pets = ['Hedwig', 'Scabber', 'Crookshank']
for wiz, pet in zip(wizards, pets):
    print(f'{wiz} has {pet}')
for index, (wiz, pet) in enumerate(zip(wizards, pets)):
    print(f'{index}. {wiz} has {pet}')
sortedByFirst = sorted(['hi', 'hello', 'phuong', 'pham'], key=lambda el:el[1])
print(sortedByFirst)
sortedByKey = sorted([{'name': 'Phuong Pham', 'age' : 20}, {'name': 'Daniel', 'age' : 21}, {'name': 'Willson', 'age': 35}], key=lambda el:el['name'])
print(sortedByKey)

#2D List
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])
#listConverted = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
#print(listConverted)
print([x for x in zip(*matrix)])