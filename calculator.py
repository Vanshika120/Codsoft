from tkinter import *
root=Tk()
root.geometry("570x540")
root.title("CALCULATOR")
#functions on buttons
def click_button(num):
    global exp 
    exp=exp+str(num)
    input_text.set(exp)
def clear_button():
    global exp 
    exp=""
    input_text.set("")
def equal_button():
    global exp 
    r=str(eval(exp))
    input_text.set(r)
    exp=""
exp=""
input_text=StringVar()
#frame widget and input field
input_frame = Frame(root, width = 550, height = 100, bd = 0, highlightbackground = "brown", highlightcolor = "black", highlightthickness = 2)
input_frame.pack(side = TOP)
input_field = Entry(input_frame, font = ('arial', 20, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 20)
btns_frame = Frame(root, width = 550, height = 520,highlightbackground ="brown",highlightthickness =3, bg = "black")
btns_frame.pack()
#placing buttons 
#first row
seven = Button(btns_frame, text = "7", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(7)).grid(row = 0, column = 0, padx = 2, pady = 2)
eight = Button(btns_frame, text = "8", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(8)).grid(row = 0, column = 1, padx = 2, pady = 2)
nine = Button(btns_frame, text = "9", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(9)).grid(row = 0, column = 2, padx = 2, pady = 2)
multiply = Button(btns_frame, text = "*", fg = "black",font=('arial',15,'bold'), width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("*")).grid(row = 0, column = 3, padx = 2, pady = 2)
#second row
four = Button(btns_frame, text = "4", fg = "black", font=('arial',15,'bold'),width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(4)).grid(row = 1, column = 0, padx = 2, pady = 2)
five = Button(btns_frame, text = "5", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(5)).grid(row = 1, column = 1, padx = 2, pady = 2)
six = Button(btns_frame, text = "6", fg = "black", font=('arial',15,'bold'),width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(6)).grid(row = 1, column = 2, padx = 2, pady = 2)
minus = Button(btns_frame, text = "-", fg = "black",font=('arial',15,'bold'), width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("-")).grid(row = 1, column = 3, padx = 2, pady = 2)
#third row
one = Button(btns_frame, text = "1", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(1)).grid(row = 2, column = 0, padx = 2, pady = 2)
two = Button(btns_frame, text = "2", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(2)).grid(row = 2, column = 1, padx = 2, pady = 2)
three = Button(btns_frame, text = "3", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(3)).grid(row = 2, column = 2, padx = 2, pady = 2)
plus = Button(btns_frame, text = "+", fg = "black",font=('arial',15,'bold'), width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("+")).grid(row = 2, column = 3, padx = 2, pady = 2)
#fourth row
zero = Button(btns_frame, text = "0", fg = "black",font=('arial',15,'bold'), width = 23, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: click_button(0)).grid(row = 3, column = 0,columnspan=2 , padx = 2, pady = 2)
point = Button(btns_frame, text = ".", fg = "black",font=('arial',15,'bold'), width = 11, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button(".")).grid(row = 3, column = 2, padx = 2, pady = 2)
divide=Button(btns_frame, text="/", fg="black",font=('arial',15,'bold'),width=10, height=3, bd=0, bg="#eee", cursor="hand2",command= lambda: click_button("/")).grid(row=3, column= 3, padx=2, pady=2)
#fifth row
equals = Button(btns_frame, text = "=", fg = "black",font=('arial',15,'bold'), width = 23, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: equal_button()).grid(row = 4, column = 0,columnspan=2, padx = 2, pady = 2)
clear = Button(btns_frame, text = "Clear", fg = "black",font=('arial',15,'bold'), width = 22, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clear_button()).grid(row = 4, column = 2, columnspan = 2, padx = 2, pady = 2)
#end of program
root.mainloop()

