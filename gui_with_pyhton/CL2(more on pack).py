from tkinter import *
root=Tk()
frame1=Frame(root) # this creates a frame , a frame is like a div in Html
# frame2=Frame(frame1)
# frame2.pack()
b1=Button(frame1,text="cleck me",command=root.destroy
          ,background="Red",fg="white") # we are creating an button inside a frame. here we have use the property of the button class in tkinter like background to give a color to it and fg to give color to the text inside it.
# frame1.pack(fill=BOTH,expand=True)
b2=Button(frame1,text="cleck me as well",command=frame1.destroy,background="pink",fg="red")

frame1.pack()
b1.pack(side="left",expand=True,fill=BOTH)  # this will close the entier window
b2.pack(side="left",expand=True,fill=BOTH)# this will close the frame 1 only

root.mainloop()
