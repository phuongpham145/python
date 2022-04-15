print(range(1, 3))
print(range(4))
for i in range(4):
    print(i)
for i in range(1, 3):
    print(i)
list = [1, 2, 3, 1, 2, 8]
for i in range(len(list)):
    print(list[i])
for x in list:
    print(x)
for i, value in enumerate(list):
    print(i, value)
for i in range(10):
    if i % 3 == 0:
        continue
    print(i)
    if i%5 == 0 and i > 0:
        break
dates = [1982, 1980, 1973, 2000]
i = 0
year = 0
while(year != 1973):
    year = dates[i]
    i += 1
    print(year)
print("It took", i, "repetitions to get out of loop.")