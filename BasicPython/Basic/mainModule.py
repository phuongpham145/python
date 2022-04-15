from phuongPham import emailProcess, printMsg

def main():
    emails = ['phuongpham@gmail.com', 'danielpham@vnuis.edu.vn']
    for email in emails:
       userName, domain = emailProcess(email)
       printMsg(userName, domain)
if __name__ == "__main__":
    main()

