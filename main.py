import tkinter as tk
import todo_logic as logic

def retrieve():
    listbox.insert(listbox.size(), newTask.get())


root = tk.Tk()
root.geometry("900x600")
root.config(background="black")

frame = tk.Frame(root, bg='pink')
frame.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)

canvas = tk.Canvas(root, height= 450, width= 200, bg='black')
canvas.pack(side='left', padx=40)



listbox = tk.Listbox(frame)
listbox.pack()

button = tk.Button(frame, text="Add Task", highlightbackground='green', fg="black", command=retrieve)
button.pack(padx = 5, pady = 5)

newTask = tk.Entry(frame, width = 20, highlightbackground='green', fg="green")
newTask.insert(0,'To-Do Item')
newTask.pack(padx = 5, pady = 0)


root.mainloop()
