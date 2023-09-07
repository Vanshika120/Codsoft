import tkinter as tk                      
from tkinter import ttk                 
from tkinter import messagebox           
import sqlite3 as sql                  
  
# defining the function  
def add_task():   
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.askokcancel('No task entered','Enter task')  
    else:  
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values(?)', (task_string ,))  
        list_update()  
        task_field.delete(0, 'end')  
def list_update():  
    clear_list()  
    for task in tasks:  
        listbox.insert('end', task)  
def delete_task():  
    try:  
        the_value = listbox.get(listbox.curselection())   
        if the_value in tasks:  
            tasks.remove(the_value)  
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:    
        messagebox.askokcancel('No task selected','Select task')        
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:   
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  
def clear_list():   
    listbox.delete(0, 'end')  
def close():   
    print(tasks)  
    root.destroy()    
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):   
        tasks.append(row[0])  
  
# creating windows and labels
if __name__=="__main__" :
    root = tk.Tk()   
    root.title("To-Do List Manager ")  
    root.geometry("500x450+750+250")
    root.resizable(0,0)  
    root.configure(bg = "#FAEBD7")  
    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
    tasks = []  
    header_frame = tk.Frame(root, bg = "brown") 
    header_frame.pack(fill = "both") 
    functions_frame = tk.Frame(root, bg = "brown")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame = tk.Frame(root, bg = "brown")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
    header_label = ttk.Label(header_frame, text = " To-Do List",font = ("Brush Script MT", "35"),background = "brown",foreground = "green")  
    header_label.pack(padx = 20, pady = 20)  
    task_label = ttk.Label(   functions_frame, text = "Enter the Task:", font = ("arial", "15", "bold"), background = "brown",foreground = "#000000")  
    task_label.place(x = 30, y = 40)  
    task_field = ttk.Entry(functions_frame,font = ("arial", "13"),width = 20, background = "#FFF8DC", foreground = "#A52A2A")  
    task_field.place(x = 30, y = 80)  
  
# adding buttons  
    add_button = tk.Button(functions_frame,text = "Add Task",width = 17,font=('arial 12 bold') ,command = add_task )
    add_button.place(x = 30, y = 120)  
    del_button = tk.Button(functions_frame, text = "Delete Task", width = 17,font=('arial 12 bold'),command = delete_task ) 
    del_button.place(x = 30, y = 170)  
    del_all_button = tk.Button(functions_frame,  text = "Delete All Tasks", width = 17,font=('arial 12 bold'), command = delete_all_tasks)  
    del_all_button.place(x = 30, y = 220)  
    exit_button = tk.Button(functions_frame,text = "Exit", width = 17, font=('arial 12 bold'),command = close)  
    exit_button.place(x = 30, y = 270)

  #creating listbox
    listbox = tk.Listbox(listbox_frame,  width = 30,height = 20,selectmode = 'SINGLE',  background = "#FFFFFF",  foreground = "#000000",  selectbackground = "#CD853F",selectforeground = "#FFFFFF")  
    listbox.place(x = 10, y = 20)  
    retrieve_database()  
    list_update()  
    root.mainloop()  
    the_connection.commit()  
    the_cursor.close()  