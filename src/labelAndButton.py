import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('200x100')

# text 关键字参数和 textvariable是冲突的
# l = tk.Label(window, text='my god, this is tk', bg='green',
#              font=('Arial', 12), width=15, height=2)

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green',
             font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False


# 函数前要放两个空行
def hit_me():
    global on_hit
    # if on_hit == True这种方式可简写成下面的
    if on_hit:
        var.set('hit me')
        on_hit = False
    else:
        var.set('not hit me')
        on_hit = True


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
b.pack()

window.mainloop()
