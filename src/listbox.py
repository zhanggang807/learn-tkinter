import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b = tk.Button(window, text='print selection', width=15, height=2,
              command=print_selection)
b.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)

list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)  # 从后面插入

lb.insert(1, 'first')
lb.insert(2, 'second')  # 指定索引插入
lb.delete(2)  # 删除
lb.pack()

window.mainloop()
