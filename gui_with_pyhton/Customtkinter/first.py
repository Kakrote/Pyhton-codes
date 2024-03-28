# importing customtkinter
from typing import Tuple
import customtkinter as ctk
appwidth=600
apphight=700
# seting the temes and mode of the window
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
# creating a class for the app
class App(ctk.CTk):
    def __init__(self,*arrgs, **kwargs):
        super().__init__(*arrgs, **kwargs)
        # setting the defult geomerty of the window and the title of the window
        self.title("Main app")
        self.geometry(f"{appwidth}x{apphight}")
        # now we have to add the lables to the window
        self.nameLable=ctk.CTkLabel(self,text="Name")
        self.nameLable.grid(row=0,column=0,padx=20,pady=20,sticky='ew')
        # adding the entry wigit
        self.nameEntry=ctk.CTkEntry(self,placeholder_text="enter your name",font=("times new roman",12))
        self.nameEntry.grid(row=0,column=1,pady=20,sticky='ew')
        # creating a button
        self.button=ctk.CTkButton(self,text="submit",command=self.genratext)
        self.button.grid(row=1,column=0,padx=20,pady=20,sticky='ne')
        # to display
        self.displaybox=ctk.CTkTextbox(self,width=200,height=300)
        self.displaybox.grid(row=3,column=0,columnspan=8,padx=20,pady=20,sticky='nsew')
    def genratext(self):
        self.displaybox.delete('0.0')
        text=self.create()
        self.displaybox.insert('0.0',text)
    def create(self):
        import time as t
        self.name=self.nameEntry.get()
        text=t.localtime(t.time())
        return f"{self.name}   {text.tm_min}:{text.tm_sec}\n"

if __name__=="__main__":
    app=App()
    app.mainloop()