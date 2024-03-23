# creating the basic window for the trying perpose.
from tkinter import *
root=Tk()
#  inside this we will create the logic  and everything for the app window.
root.minsize(200,200) # gives the minimum size to the window to be opean 
root.maxsize(1000,1000) # provide the maximum size to the window to be opean which cant be exeed 
# now creating the lable in the tkinter
var=Label(text="This is a sample gui window and it does nothing .")
var.pack() # this pack the var into the window.
Button=Button(root,text="stop",command=root.destroy,width=20) # this create a button into the window.
Button.pack() # the pack function helps in packing things in grid.
root.mainloop()