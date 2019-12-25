"""
Author: Ayo Asekun
Date Created: Dec 3rd, 2019
Last Date Modified: Dec 3rd, 2019
Program Description: Creating a Temperature Converter Using Tkinter
Psuedocode:
<START PROGRAM>
Inputs: User chooses which entry box to use
        Fahrenheit input; to convert to celsius
        Celsius input; to convert to Fahrenheit
Process: User inputs information as directed by Program
         Using provided formulas, depending on which conversion is being requested,
         program will run against input to produce required output
        FORMULAS -
            Celsius: (Entry Value * 1.8) + 32
            Fahrenheit: (Entry Value - 32) * 0.56
Output: Converted values from provided entry provided by user
        From °C to °F
             OR
        From °F to °C

<END PROGRAM>
"""
from tkinter import*

def fahr():
    # fahrenheit conversion function
    words = fbtext.get()
    ftemp = float(words)
    celbox.delete(0, END)
    celbox.insert(0, "%.2f" % (tocel(ftemp)))                                   # rounded to 2 decimal
    return
def cel():
    # Celsius conversion function
    entry = cbtext.get()
    ctemp = float(entry)
    fahrbox.delete(0, END)
    fahrbox.insert(0, "%.2f" % (tofahr(ctemp)))                                 # rounded to 2 decimal
    return


"""FORMULAS"""
# Conversion formulas for Fahrenheit & Celsius
def tocel(fahr):
    return (fahr * 1.8) + 32
def tofahr(cel):
    return (cel - 32) * 0.56


"""CLEAR BUTTON"""
def clear():
    # clear entries function
    celbox.delete(0, "end")
    fahrbox.delete(0, "end")
    return None


"""MAIN WINDOW FOR TEMPERATURE CONVERTER"""
TC = Tk()
TC.title("Temperature converter")
TC.configure(bg="black", relief=SUNKEN, borderwidth=8)
TC.geometry("350x100")
TC.columnconfigure(1, weight=1)
TC.rowconfigure(1, weight=1)

"""LABELS SETUP & GRID"""
# Labels for Celsius entry.....
cellabel = Label(TC, text="CELSIUS", bg="black", foreground="blue")
cellabel.grid(row=0, column=0)
# Labels for Fahrenheit entry
fahrlabel = Label(TC, text="FAHRENHEIT", bg="black", foreground="red")
fahrlabel.grid(row=1, column=0)

"""STORE ENTRY VALUES"""
# Storing user entry for Fahrenheit input
fbtext = StringVar()
fbtext.set(" ")
fahrbox = Entry(TC, textvariable=fbtext, borderwidth=5, relief=SUNKEN)
fahrbox.grid(row=0, column=1)
# Storing user entry for Celsius input
cbtext = StringVar()
cbtext.set(" ")
celbox = Entry(TC, textvariable=cbtext, borderwidth=5, relief=SUNKEN)
celbox.grid(row=1, column=1)

"""BUTTONS GRID"""
# Fahrenheit Convert Button
f_button = Button(TC, text="Convert", command=fahr)
f_button.grid(row=0, column=2)
# Celsius Convert Button
c_button = Button(TC, text="Convert", command=cel)
c_button.grid(row=1, column=2)
# Clear contents in entry boxes
clr_button = Button(TC, text="CLEAR", command=clear, bg="red")
clr_button.grid(row=2, column=1)

TC.mainloop()
