import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file='ins.gif')  # 类型支持问题
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
# anchor 锚定点，以图片上某个位置为原点
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1)
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
canvas.pack()


def move():
    canvas.move(rect, 0, 2)


b = tk.Button(window, text='move', command=move).pack()

window.mainloop()
