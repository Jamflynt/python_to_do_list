from tkinter import messagebox, Tk, Listbox, Entry, Button, END, RIGHT, Y, Scrollbar, Frame

root = Tk()
root.title("To-Do List")


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(END, task)
        entry_task.delete(0, END)
    else:
        messagebox.showwarning(message="Please enter a task.")


def delete_task():
    pass

def load_tasks():
    pass

def  save_tasks():
    pass


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox_task = Listbox(root, height=10, width=50)
listbox_task.config(yscrollcommand=scrollbar.set)
listbox_task.pack()

scrollbar.config(command=listbox_task.yview)

entry_task = Entry(root, width=50)
entry_task.pack()

button_add_task = Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = Button(root, text="Load Task", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = Button(root, text="Save Task", width=48, command=save_tasks)
button_save_tasks.pack()


root.mainloop()