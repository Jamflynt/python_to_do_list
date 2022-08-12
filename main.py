from tkinter import messagebox, Tk, Listbox, Entry, Button, END, RIGHT, Y, Scrollbar, Frame
import pickle

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
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        messagebox.showwarning(message="Please select a task to delete.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_task.delete(0, END)
        for task in tasks:
            listbox_task.insert(END, task)
    except:
        messagebox.showwarning(message="No save file on disk. Please save tasks first before loading.")


def save_tasks():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


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