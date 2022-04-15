import string
import random
LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation
def passwordGenerator(length = 8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)
    ranomPassword = random.choices(printable, k = length)
    ranomPassword = ''.join(ranomPassword)
    return ranomPassword
def getPasswordLength():
    passwordLength = input("How long do you want your password: ")
    return int(passwordLength)
def main():
    passwordLength = getPasswordLength()
    password = passwordGenerator(passwordLength)
    print(password)
if __name__ == '__main__':
    main()