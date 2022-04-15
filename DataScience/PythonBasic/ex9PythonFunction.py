def add(a, b):
    return a + b
a = 3
b = 4
res = add(a, b)
print("res: ", res)
def show():
    print("Show Function")
show()
def showValue(value):
    if value % 2 == 0:
        print(value, " is even number")
    else:
        print(value, " is odd number")
showValue(30)
def sumDigits(value):
    res = 0
    while value > 0:
        res += (value % 10)
        value //= 10
    return res
def showDigits(a):
    tmp = sumDigits(a)
    if tmp % 2 == 0:
        print(tmp, " is even number")
    else:
        print(tmp, " is odd number")
showDigits(3455)