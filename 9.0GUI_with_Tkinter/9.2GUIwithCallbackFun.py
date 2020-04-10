from tkinter import *

window = Tk()

# Entry
entry_value = StringVar()
entry1 = Entry(window, textvariable=entry_value)
entry1.grid(row=0, column=1)

# Text widgets
txt1 = Text(window, height=1, width=20)
txt1.grid(row=0, column=2)

# Fun
def km_to_miles():
    # print(entry_value.get())
    miles = float(entry_value.get())*1.6
    txt1.insert(END, miles)

# call the method without '()'
btn = Button(window, text="Execute", command=km_to_miles)
btn.grid(row=0, column=0)

window.mainloop()