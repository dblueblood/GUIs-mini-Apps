from tkinter import*

def NSC():
    import os
    path = ""
    # Path to file or website for template to new case ticket
    NSC1 = os.startfile(path)
# Existing ticket template
def ESC():
    import os
    path = ""
    # path to file or website for template to existing case ticket
    ESC1 = os.startfile(path)


"""MAIN WINDOW FOR SERVICE LOGS TEMPLATE"""
TC = Tk()
TC.title("SERVICE REQUEST TEMPLATES")
TC.configure(bg="GREY", relief=SUNKEN, borderwidth=3)
TC.geometry("350x100")
TC.columnconfigure(1, weight=1)
TC.rowconfigure(1, weight=1)

"""LABELS SETUP & GRID"""
# Labels for Celsius entry.....
newlabel = Label(TC, text="NEW SERVICE REQUEST", bg="grey", fg="white")
newlabel.grid(row=0, column=0)
# Labels for Fahrenheit entry
extlabel = Label(TC, text="EXT. SERVICE REQUEST", bg="grey", fg="white")
extlabel.grid(row=1, column=0)

"""BUTTONS GRID"""
# Existing Service Request
N_button = Button(TC, text="NEW TEMPLATE", command=NSC, relief=RAISED, bg="red")
N_button.grid(row=0, column=2)
# New Service Request
E_button = Button(TC, text="EXT. TEMPLATE", command=ESC, relief=RAISED, bg="blue")
E_button.grid(row=1, column=2)
# Clear contents in entry boxes

TC.mainloop()
