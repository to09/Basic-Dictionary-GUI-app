from backend import *
from tkinter import *

def front():
    #finding input word in dictionary
    def search_command():
        msg = enter_word.get()
        y_n_responce = enter_responce.get()
        definition1 = translate(msg)
        if y_n_responce != "Enter 'Y' or 'N'":
            definition1 = get_responce(y_n_responce, msg)
        if definition1 == "Not found word":
            display_msg = match(msg)
            display_result(display_msg)
            return
        display_result(definition1)

    #addind favourite word to database
    def Favourite_command():
        insert(enter_word.get())
        list1.delete(0,END)
        message  = enter_word.get() + " added succsessfully"
        list1.insert(END, message)

    #view favorite word in database
    def view_command():
        list1.delete(0,END)
        for row in view():
            list1.insert(END, row)

    def clear_search(event):
        search.delete(0, END)

    #display matching words from dictionary
    def display_result(definition1):
        list1.delete(0,END)
        if type(definition1) == list:
            count = 0
            for item in definition1:
                count += 1
                output = str(count) + " : " + item + "\n"
                list1.insert(END, output)
        else:
            list1.insert(END, definition1)

    #code for the GUI (front end)
    window = Tk()
    window.wm_title("Basic Dictionary")
    l1 = Label(window, text="Basic English Dictionary ", bg="dark grey", font=("Times", 20, "bold"))
    l1.grid(row=0, column =0,columnspan = 6)

    l2 = Label(window, text="Enter word", font=("Times", 14))
    l2.grid(row = 1, column = 0)

    enter_word = StringVar()
    e1 = Entry(window, textvariable = enter_word)
    e1.grid(row = 1, column = 1)

    enter_responce = StringVar()
    search = Entry(window, textvariable = enter_responce)
    search.insert(0, "Enter 'Y' or 'N'")
    search.grid(row = 1, column= 3)
    search.bind("<Button-1>", clear_search)

    list1 = Listbox(window, height = 6, width = 35)
    list1.grid(row = 2, column =0, rowspan = 6, columnspan = 2)
    list1.bind('<<ListboxSelect>>',search_command)

    #now we need to attach a scrollbar to the listbox, and the other direction,too
    sb1 = Scrollbar(window)
    sb1.grid(row = 2, column = 2, rowspan = 6)
    list1.config(yscrollcommand = sb1.set)
    sb1.config(command = list1.yview)

    sb2 = Scrollbar(window,orient=HORIZONTAL)
    sb2.grid(row=5, column=1)
    list1.config(xscrollcommand=sb2.set)
    sb2.config(command=list1.xview)

    b1 = Button(window, text = "Search", width = 12, command = search_command)
    b1.grid(row = 2, column = 3)

    b2 = Button(window, text = "Favourite", width = 12, command = Favourite_command)
    b2.grid(row = 3, column = 3)

    b2 = Button(window, text="View all", width=12, command=view_command)
    b2.grid(row=4, column=3)

    b3 = Button(window, text = "Close", width = 12, command = window.destroy)
    b3.grid(row = 5, column = 3)
    window.mainloop()