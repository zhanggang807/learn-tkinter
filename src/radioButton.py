import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected ' + var.get())


rb1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
rb1.pack()

rb2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
rb2.pack()

rb3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
rb3.pack()

window.mainloop()
