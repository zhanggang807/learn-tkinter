import tkinter as tk
import tkinter.messagebox
# 为什么我这里要导入？网上好多的关于消息框的方法，为什么不统一？

window = tk.Tk()
window.title('my window')
window.geometry('200x300')


def hit_me():
    # tk.messagebox.showinfo(title=' hi ', message='info message')
    # tk.messagebox.showwarning(title=' hi ', message='warning message')
    # tk.messagebox.showerror(title=' hi ', message='error message')
    # print(tk.messagebox.askquestion(title=' hi ', message='error message'))  # 返回yes或者no
    # print(tk.messagebox.askyesno(title=' hi ', message='error message'))  # 返回True或者False
    # print(tk.messagebox.askretrycancel(title='hi', message='retry cancel'))
    print(tk.messagebox.askokcancel(title='hi', message='ok cancel'))


tk.Button(text='hit me', command=hit_me).pack()

window.mainloop()
