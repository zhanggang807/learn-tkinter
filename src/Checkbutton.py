import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


# 这里是有传入值的
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='i love only python')  # 这里可以替换成对象的text值吗
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='i love only c++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='i do not love either')
    elif (var1.get() == 1) & (var2.get() == 1):
        l.config(text='i love both')


var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()

c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c2.pack()

window.mainloop()
