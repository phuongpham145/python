def cToFConverter():
    while True:
        cTemp = input("Please enter C degree : ")
        if cTemp:
         cTemp = float(cTemp)
         fTemp = round(9*cTemp / 5 + 32)
         print(f"{cTemp}C is converted to {fTemp}F")
         break
        else:
         print("No Data !")
         continue
def main():
    #print("Hello World")
    cToFConverter()
if __name__ == "__main__":
    main()