def emailProcess(email):
    userName = email[0:email.index("@")]
    domain = email[email.index("@") + 1:]
    return[userName, domain]
def printMsg(userName, domain):
    print(f"Username is {userName}; Domain is {domain}")
def main():
    email = input("Please input your email: ").strip()
    userName, domain = emailProcess(email)
    printMsg()
if __name__ == "__main__":
    main()