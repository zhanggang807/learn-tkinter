import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# e = tk.Entry(window, show='*')
e = tk.Entry(window, show=None)
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert('2.2', var)
    # 某行某列输入,指定点输入


b = tk.Button(window, text='insert ponint', width=15, height=2, command=insert_point)

b.pack()

b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

t = tk.Text(window, height=2, bg='red')
t.pack()

window.mainloop()
