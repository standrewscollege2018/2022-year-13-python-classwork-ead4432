''' Intro to tkinter'''

def say_hello():
    if message.get() == "Thanks":
        message.set("z")
    else:
        message.set("Thanks")

def print_input():
    user = input("What'd you want to do")
    print(user)
#import
from tkinter import *

root = Tk()
root.title = ("My first tkinter")
root.resizable(width= False, height= False)
root.geometry("800x500")
root.configure(bg="#123456")

#Add a label
heading_lbl = Label(root, text="test comic sans", fg="red", font=("Comic Sans MS", 25))
heading_lbl.grid(row=0, column=0)

#set up label for hello
#set up stringVar
message = StringVar()
message_lbl = Label(root, textvariable=message)
message_lbl.grid(row=1, column=1)

#Add button
pushme_btn = Button(root, text="Push me!", width=30, height=5, command=say_hello)
pushme_btn.grid(row=1, column=2)

#Add button
get_btn = Button(root, text="Get me!", width=30, height=5, command=print_input)
get_btn.grid(row=2, column=0)

input_field_btn = Entry(root)
input_field_btn.grid(row=2, column=1)

root.mainloop()