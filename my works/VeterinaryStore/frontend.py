from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)
        e6.insert(END,selected_tuple[6])
        e7.delete(0,END)
        e7.insert(END,selected_tuple[7])
        e8.delete(0,END)
        e8.insert(END,selected_tuple[8])
    except IndexError:
        pass
    
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(name_text.get(), owner_text.get(), kind_text.get(), age_text.get(), arrival_text.get(), departure_text.get(), status_text.get(), comment_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(name_text.get(), owner_text.get(), kind_text.get(), age_text.get(), arrival_text.get(), departure_text.get(), status_text.get(), comment_text.get())
    list1.delete(0, END)
    list1.insert(END, (name_text.get(), owner_text.get(), kind_text.get(), age_text.get(), arrival_text.get(),departure_text.get(), status_text.get(), comment_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],name_text.get(), owner_text.get(), kind_text.get(), age_text.get(), arrival_text.get(), departure_text.get(), status_text.get(), comment_text.get(),)

window = Tk()

window.wm_title("Veterinary Database")

l1 = Label(window,text = "Name")
l1.grid(row = 0,column = 0)

l2 = Label(window,text = "Owner")
l2.grid(row = 0,column = 2)

l3 = Label(window,text = "Kind")
l3.grid(row = 1,column = 0)

l4 = Label(window,text = "Age")
l4.grid(row = 1,column = 2)

l5 = Label(window,text = "Arrival")
l5.grid(row = 2,column = 0)

l6 = Label(window,text = "Departure")
l6.grid(row = 2, column = 2)

l7 = Label(window, text = "Status")
l7.grid(row = 3, column = 0)

l8 = Label(window,text = "Comment")
l8.grid(row = 3,column = 2)

# Entry for the variables
name_text = StringVar()
e1 = Entry(window, textvariable = name_text)
e1.grid(row = 0, column = 1)

owner_text = StringVar()
e2 = Entry(window, textvariable = owner_text)
e2.grid(row = 0, column = 3)

kind_text = StringVar()
e3 = Entry(window, textvariable = kind_text)
e3.grid(row = 1, column = 1)

age_text = StringVar()
e4 = Entry(window, textvariable = age_text)
e4.grid(row = 1, column = 3)

arrival_text = StringVar()
e5 = Entry(window, textvariable = arrival_text)
e5.grid(row = 2, column = 1)

departure_text = StringVar()
e6 = Entry(window, textvariable = departure_text)
e6.grid(row = 2, column = 3)

status_text = StringVar()
e7 = Entry(window, textvariable = status_text)
e7.grid(row = 3, column = 1)

comment_text = StringVar()
e8 = Entry(window, textvariable = comment_text)
e8.grid(row = 3, column = 3)


# Other features
list1=Listbox(window, height = 7, width = 35)
list1.grid(row = 4, column = 0, rowspan = 7, columnspan = 2)

sb1=Scrollbar(window)
sb1.grid(row = 4,column = 2, rowspan = 7)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,text="Refresh", width = 12, command = view_command)
b1.grid(row = 4, column = 3)

b2=Button(window,text="Search Pet", width = 12, command = search_command)
b2.grid(row = 5,column = 3)

b3=Button(window,text="Add Pet", width = 12, command = add_command)
b3.grid(row = 6, column = 3)

b4=Button(window,text="Update Entry", width = 12, command = update_command)
b4.grid(row = 7, column = 3)

b5=Button(window,text = "Delete Entry", width = 12, command = delete_command)
b5.grid(row = 8, column = 3)

b6=Button(window,text = "Close", width = 12, command = window.destroy)
b6.grid(row = 9, column = 3)

window.mainloop()
