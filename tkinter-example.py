import tkinter as tk
from tkinter import * #change to specifics when I know what i want

def set():
    print("set() run")
    labelText.set(labelText.get() + "+")

def retrieve():
    print(newTask.get())

root = tk.Tk()
root.geometry("900x500")
root.title("ToDo")
frame = tk.Frame(root)
frame.pack()

labelText = tk.StringVar()
labelText.set("Initial Text")
label = tk.Label(root, textvariable = labelText)
label.pack()

button = tk.Button(root, text = "Change Label Text", command = set)
button.pack()

newTask = Entry(root, width = 20)
newTask.insert(0,'To-Do Item')
newTask.pack(padx = 5, pady = 5)

button = tk.Button(root, text = "add task", command = retrieve)
button.pack()



root.mainloop()
