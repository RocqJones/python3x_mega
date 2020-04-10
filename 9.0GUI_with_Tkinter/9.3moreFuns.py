"""
    TASK.
    Create a Python program that expects a kilogram input value and converts that value to grams, pounds, and ounces when the user pushes the convert button.
    Tip:
    1 kg = 1000 grams
    1 kg = 2.20462 pounds
    1 kg = 35.274 ounces
"""

from tkinter import *

window = Tk()

# label
e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)

# entry
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

# convery fun


def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    # txt widget 1
    t1.delete("1.0", END)
    t1.insert(END, gram)
    # txt widget 2
    t2.delete("1.0", END)
    t2.insert(END, pound)
    # txt widget 3
    t3.delete("1.0", END)
    t3.insert(END, ounce)


# btn
b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=0, column=2)

# 3 Text widgets
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()