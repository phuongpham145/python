
def printName(name):
    print(name)
def varibleLenghArgs(a, b, *args, **kwargs):
    print(a, b, *args)
    for arg in args:
        print(arg)
    for key, val in kwargs.items():
        print(key, val)
def main():
    printName("Phuong")
    #varibleLenghArgs('a', 'b', 'HelloWord', 1, 2, 3)
    varibleLenghArgs('a', 2, 'HelloWord', 1, size = "Up size", age = "NG")

if __name__ == '__main__':
    main()