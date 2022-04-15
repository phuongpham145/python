myString = 'Hello World'
print(type(myString))
char = myString[0] #-1, -2, ... cuoi
print(char)
#subtring with slicing
subString = myString[1:5]
print(subString)
# Dao nguoc string
reverseString = myString[::-1]
print(reverseString)
#take every second chracter
secondString = myString[::2]
print(secondString)
#concatenate string
myList = ['How', 'are', 'you', 'doing ?']
sentense = ' '.join(myList)
print(sentense)

for char in myString:
    print(char)
if 'X' in myString:
    print("Yes")
else:
    print("No")
#Mot so ham co ban
print("     I am alone    ".strip())
print("on an island".strip('o'))
print('but life is good'.split())
print('but, very boring'.split(','))
print('Help me'.replace("me", "you"))
print(myString.startswith('Hello'))
print(myString.endswith('need'))
print(myString.index('o'))
print(myString.find('W'))
print(myString.upper())
print(myString.lower())
print(myString.title())
print(myString.capitalize())
print(myString.count('o'))
#Formatting
pi = 3.145
name = "Phuong Pham"
tittle = "Welcome to %s %f" % (name, pi) # co the la so
print(tittle)

age = 24
height = 170.5
myString1 = "I am {} years old, {:.3f} cm".format(age, height)
print(myString1)

myString2 = f"Pi is {pi:.2f} and my name is {name}, {age} years old"
print(myString2)