# import everything with '*'
from tkinter import *

# create a window
window = Tk()

# Other code goes in btwn
btn1 = Button(window, text="Execute")
# btn1.pack()
btn1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

entry1 = Text(window, height=1, width=20)
entry1.grid(row=0, column=2)

# close window - Allows you to have an exit button
window.mainloop()