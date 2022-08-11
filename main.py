from tkinter import messagebox, Tk, Listbox, Entry, Button

root = Tk()
root.title("To-Do List")


def add_task():
    pass


listbox_task = Listbox(root, height=3, width=50)
listbox_task.pack()

entry_task = Entry(root, width=50)
entry_task.pack()

b_add_task = Button(root, text="Add Task", width=48, command=add_task)
b_add_task.pack()

root.mainloop()