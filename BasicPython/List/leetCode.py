myList = input("Enter your list: ")
def isPalindrome(s : str) -> bool:
    if s:
        result = []
        for c in s.lower():
            if c.isalnum():
                result.append(c)
        return result == result[::-1]
    else:
        return True
def main():
    print(isPalindrome(myList))
if __name__ == '__main__':
    main()