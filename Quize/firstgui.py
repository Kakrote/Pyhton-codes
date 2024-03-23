import tkinter as tk
r=tk.Tk() # this creats the main window of the program.
r.title("stoping program") # this is to give the title to the frame 
button=tk.Button(r,text="fuckoff",width=32,command=r.destroy) # create a button 
button.pack() # packs every thing in the window.
r.mainloop() # this mainloop function helps to run the frame in the runtime