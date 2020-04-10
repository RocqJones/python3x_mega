"""
    A program that stores book information:
    - Title, Author
    - Year, ISBN
    
    User can View, Search, Add entry, Update entry, delete, and close app

"""
from tkinter import *
import backend



# 3.0 Connect frontend and backend
def view_btn():
    lbox1.delete(0,END) # This will ensure that when you click view all btn it executes once
    for row in backend.view():
        lbox1.insert(END,row)

def search_btn():
    lbox1.delete(0,END)
    # iterate through backend
    for row in backend.search(title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get()):
        lbox1.insert(END, row)

def add_btn():
    backend.insert(title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get())
    lbox1.delete(0,END)
    lbox1.insert(END, (title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get()))

def get_selected_row(event):
    global selected_tuple # 'selected_tuple' we make it global to be accessed in another funtion
    index = lbox1.curselection()[0] # curselection returns indices of currently selected item.
    selected_tuple = lbox1.get(index)
    # let's fill entries with selected items
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def delete_btn():
    backend.delete(selected_tuple[0])

def update_btn():
    backend.update(selected_tuple[0], title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get())

# 1.0 create GUI
window = Tk()

window.wm_title("BookStore")

# creating labels: Title, Author, Year, and ISBN
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# add entries
title_txt = StringVar()
e1 = Entry(window, textvariable=title_txt)
e1.grid(row=0, column=1)
author_txt = StringVar()
e2 = Entry(window, textvariable=author_txt)
e2.grid(row=0, column=3)
year_txt = StringVar()
e3 = Entry(window, textvariable=year_txt)
e3.grid(row=1, column=1)
isbn_txt = StringVar()
e4 = Entry(window, textvariable=isbn_txt)
e4.grid(row=1, column=3)

# create listbox
lbox1 = Listbox(window, height=6, width=35)
lbox1.grid(row=2, column=0, rowspan=6, columnspan=2)

# scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# add configuration to scrollbar(vertically) and listbox
lbox1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lbox1.yview)
# binding method binds a function to a widget event
lbox1.bind('<<ListboxSelect>>',get_selected_row)

# buttons
btn1 = Button(window, text="View all", width=12, command=view_btn)
btn1.grid(row=2, column=3)
btn2 = Button(window, text="Search entry", width=12, command=search_btn)
btn2.grid(row=3, column=3)
btn3 = Button(window, text="Add entry", width=12, command=add_btn)
btn3.grid(row=4, column=3)
btn4 = Button(window, text="Update", width=12, command=update_btn)
btn4.grid(row=5, column=3)
btn5 = Button(window, text="Delete", width=12, command=delete_btn)
btn5.grid(row=6, column=3)
btn6 = Button(window, text="Close", width=12, command=window.destroy)
btn6.grid(row=7, column=3)

window.mainloop()

# 2.0 write backend.py 
