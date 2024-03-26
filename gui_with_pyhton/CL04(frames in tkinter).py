from tkinter import *
root=Tk()
root.geometry("1000x1000")
def fun1():
    print("this a example to give a function to the command and to call it ")
root.title("this is example of gui using frame")
# creating a simple frame with buttons
f1=Frame(root,bg="lightgreen",borderwidth=7,relief=SUNKEN,width=200)
f1.pack_propagate(False)
f1.pack(side=LEFT,fill="y")
f2=Frame(root,bg="yellow",borderwidth=6,relief=SUNKEN,height=130)
f2.pack_propagate(False)
f2.pack(side=TOP,fill="x")
l1=Label(f1,text="menu",bg="red",fg="white",borderwidth=8,relief=RAISED)
l1.pack(side=TOP,fill="x")
b1=Button(f2,text="click me",bg="red",fg="white",command=fun1) # we dont call the function thats why we are not using () we are just passing the function to the command attribute.
b1.pack()
root.mainloop()