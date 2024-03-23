from tkinter import *
root=Tk()
root.geometry("1000x1000")
root.title("practice GUI BY Anshul Pundir")
frame=Frame(root,width=200,height=300,bg="lightgreen",borderwidth=10,relief=SUNKEN)
frame.pack_propagate(False) # this allow to not to fix the frame dimintions to the content size and will alow to adjust the size according to the usser
but1=Button(frame,text="cleck me",bg="red",fg="white")
but1.pack()
frame.pack(side=TOP,anchor="center",fill=BOTH)
footer=Frame(root,borderwidth=7,relief=RAISED,bg="pink")
lable=Label(footer,text="This is footer",font=("times new roman",9,"bold"))
lable.pack()
footer.pack(side=BOTTOM,fill=BOTH)

root.mainloop()