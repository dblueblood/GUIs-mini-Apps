from tkinter import*
from tkinter import messagebox
from datetime import datetime
FRAME = Tk()
FRAME.geometry("170x100")
def reply():
    td = datetime.now().strftime("%m-%d-%Y %H:%M:%S GMT")
    rp = messagebox.showinfo("GREETINGS", "Hello! I am Alysium\nThe Current date & time is\n" + str(td) + "\nThank You")


B = Button(FRAME, text="Click Here\nPls", command=reply)
B.place(x=50, y=30)

FRAME.mainloop()






