"""
Author: Ayo Asekun
Date Created: Oct 18th, 2019
Last Date Modified: Oct 19th, 2019
Program Description: Date-Time Application
"""

from tkinter import*
from tkinter import messagebox
from datetime import datetime
FRAME = Tk()
FRAME.title("D-T App")
FRAME.geometry("220x100")
FRAME.configure(bg="green")
FRAME.columnconfigure(2, weight=1)
FRAME.rowconfigure(1, weight=2)
def reply():
    td = datetime.now().strftime("%m-%d-%Y %H:%M:%S GMT")
    rp = messagebox.showinfo("INFO", "Hello! I am Alysium\nThe Current date & time is\n" + str(td) + "\nThank You")


B = Button(FRAME, text="Click Here\nPls", command=reply)
B.config(bg="yellow")
B.grid(row=1, column=2)

FRAME.mainloop()






