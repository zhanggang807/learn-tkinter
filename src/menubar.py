import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

l = tk.Label(window, bg='yellow', text='')
l.pack()

counter = 0


def do_job():
    global counter
    l.config(text='do' + str(counter))
    counter += 1


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='new', command=do_job)
filemenu.add_command(label='open', command=do_job)
filemenu.add_command(label='save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='edit', menu=editmenu)
editmenu.add_command(label='cut', command=do_job)
editmenu.add_command(label='copy', command=do_job)
editmenu.add_command(label='paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_separator()
filemenu.add_cascade(label='import', menu=submenu, underline=0)
submenu.add_command(label='submenu1', command=do_job)

window.config(menu=menubar)
window.mainloop()
