import tkinter as tk
def add_task():
    task=entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
def remove_task():
    try:
        index=listbox.curselection()
        listbox.delete(index)
    except:
        pass
def update_task():
    try:
        index=listbox.curselection()
        task=entry.get()
        if task :
            listbox.delete(index)
            listbox.insert(index,task)
            entry.delete(0,tk.END)
    except:
        pass

window=tk.Tk()
window.title("TO-DO LIST")

entry=tk.Entry(window)
entry.pack(pady=15)

add_button =tk.Button(window,text="Add Task",command=add_task)
add_button.pack(pady=10)

listbox=tk.Listbox(window,width=50)
listbox.pack()

update_button=tk.Button(window,text="update Task",command=update_task)
update_button.pack(pady=10)

remove_button=tk.Button(window,text="remove Task",command=remove_task)
remove_button.pack(pady=10)

window.mainloop()