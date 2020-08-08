import tkinter as tk

def set():
    print("set() run")
    labelText.set(labelText.get() + "+")

root = tk.Tk()
root.title("ToDo")

labelText = tk.StringVar()
labelText.set("Initial Text")
label = tk.Label(root, textvariable = labelText)
label.pack()

button = tk.Button(root, text = "Change Label Text", command = set)
button.pack()

root.mainloop()
