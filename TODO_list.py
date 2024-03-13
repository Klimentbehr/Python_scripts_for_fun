import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        
def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass
    
    
def mark_task_complete():
    try:
        index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(index)
        if "(Completed)" not in task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, task + "(Completed)")
    
    except IndexError:
        pass
    
    
root = tk.Tk()
root.title("Todo List Application")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_mark_task_complete = tk.Button(root, text="Mark Task as Completed", width=48, command=mark_task_complete)
button_mark_task_complete.pack()

root.mainloop()