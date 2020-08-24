import tkinter as tk

def set():
    print("set() run")
    labelText.set(labelText.get() + "+")

def retrieve():
    listbox.insert(listbox.size(), newTask.get())

root = tk.Tk()
root.geometry("900x500")
root.title("ToDo")
frame = tk.Frame(root)
frame.pack()


leftframe = tk.Frame(root)
leftframe.pack(side=tk.LEFT)

rightframe = tk.Frame(root)
rightframe.pack(side=tk.RIGHT)

listbox = tk.Listbox(leftframe)
listbox.pack()


labelText = tk.StringVar()
labelText.set("Initial Text")
label = tk.Label(root, textvariable = labelText)
label.pack()

button = tk.Button(root, text = "Change Label Text", command = set)
button.pack()

newTask = tk.Entry(leftframe, width = 20)
newTask.insert(0,'To-Do Item')
newTask.pack(padx = 5, pady = 5)

button = tk.Button(leftframe, text = "add task", command = retrieve)
button.pack()



root.mainloop()
