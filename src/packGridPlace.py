import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

# 三种放置部件的方式，用于组件布局吧

# tk.Label(window, text='top').pack(side='top')
# tk.Label(window, text='right').pack(side='right')
# tk.Label(window, text='bottom').pack(side='bottom')
# tk.Label(window, text='left').pack(side='left')

# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1).grid(row=i, column=j,padx=10,pady=10)
#         tk.Label(window, text=1).grid(row=i, column=j,ipadx=10,ipady=10)

tk.Label(window, text=12,bg='red').place(x=10, y=100, anchor='nw')

window.mainloop()
