#To do app application
import tkinter as tk
from tkinter import messagebox

# Function to add a task to the to-do list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task from the to-do list
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an Entry widget for adding tasks
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a Listbox widget to display tasks
listbox = tk.Listbox(root)
listbox.pack()

# Create buttons for adding and removing tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()

# Run the application
root.mainloop()
