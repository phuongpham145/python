from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

# Tao tkinder window
root = Tk()
root.title('Pham Translator')
root.geometry('500x630')
root.iconbitmap('logo.png')
load = Image.open('background.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)
name = Label(root, text='Pham Translator', fg='#FFFFFF', bd=0, bg='#031520')
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)
box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=20)
buttonFrame = Frame(root).pack(side=BOTTOM)


def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)


def traslate():
    INPUT = box.get(1.0, END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT, src="vi", dest="en")
    b = a.text
    box1.insert(END, b)
clearButton = Button(buttonFrame, text="Clear", font=(
    "Arial", 10, 'bold'), bg='#303030', fg="#FFFFFF", command=clear)
clearButton.place(x=150, y=310)
transButton = Button(buttonFrame, text="Translate", font=(
    "Arial", 10, 'bold'), bg='#303030', fg="#FFFFFF", command=traslate)
transButton.place(x=290, y=310)
box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.pack(pady=50)
root.mainloop()
