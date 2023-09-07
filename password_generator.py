import random,string
from tkinter import *
import pyperclip
root=Tk()
root.geometry("500x300")
root.title("PASSWORD GENERATOR")
str=StringVar()
len=IntVar()
len.set(0)
def generate():
    choices=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
              't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
              'M','N','O','P','Q','R','S','T','U','W','X','Y','Z','1','2','3','4','5','6',
              '7','8','9','0','!','#','&','*','$','@','%',',']
    password=""
    for x in range(len.get()):
        password=password+random.choice(choices)
    str.set(password)
def copyClipboard():
    random_password=str.get()
    pyperclip.copy(random_password)
frame = Frame(root, width = 500, height = 300, bg = "#eee")
frame.pack(side=TOP)
label1=Label(frame,text="Enter password length",font=('calibri',20, 'bold'),bg="#eee")
label1.pack(pady=7)
e=Entry(frame,textvariable=len,font = ('arial', 10, 'bold'), width=23,bg="#eee")
e.pack(pady=5)
b=Button(frame, text="Generate Password",font = ('arial', 13, 'bold'), command=generate,bg="white")
b.pack(pady=10)
e1=Entry(frame, textvariable=str,font = ('arial', 10, 'bold'),width=23,bg="#eee")
e1.pack(pady=10)
b1=Button(frame, text="Copy to clipboard", command=copyClipboard,font = ('arial', 13, 'bold'),bg="white")
b1.pack(pady=10)
root.mainloop()