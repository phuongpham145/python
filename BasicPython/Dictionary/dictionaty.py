myDict = {"name": "PhuongPham", "content": "President", "City": "Haiduong"}
print(myDict)
myDict2 = dict(name = "PhamVanPhuong", content = "Hello everyone", city = "Binhgiang")
print(myDict2)

#Access items
contentDict = myDict["content"]
print(contentDict)
if "name" in myDict:
    print(myDict['name'])
else:
    print("No key found")
try:
    print(myDict["age"])
except KeyError:
    print("No key found")

#Add and change items
myDict["email"] = "phuongpham@gmail.com"
myDict["email"] = "phuongpham145@gmail.com"
print(myDict)
del myDict["City"]
print(myDict)
print("Pop value: " + myDict2.pop("city"))
print(myDict2)

#loop over keys
for key in myDict.keys():
    print(key, myDict[key])
for value in myDict.values():
    print(value)
for key, value in myDict.items():
    print(key, value)