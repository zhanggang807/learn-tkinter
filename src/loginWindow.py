import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('welcome to Dean Python')
window.geometry('450x300')

canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')  # 类型支持问题
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='user name:').place(x=50, y=150)
tk.Label(window, text='password:').place(x=50, y=190)

var_user_name = tk.StringVar()
var_user_name.set('example@python.com')  # 这样可以设置默认值
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=160, y=150)

var_password = tk.StringVar()
entry_password = tk.Entry(window, textvariable=var_password,show='*')
entry_password.place(x=160, y=190)


def user_login():
    print('login')
    usr_name = var_user_name.get()
    usr_pwd = var_password.get()
    print('username=' + usr_name)
    print('password=' + usr_pwd)
    if (len(usr_name) == 0) or (len(usr_pwd) == 0):
        tkinter.messagebox.showwarning(title='warning', message='name or pwd can not be empty')


def user_sign_up():
    print('sign up')


# login and sign up button
btn_login = tk.Button(window, text='login', command=user_login)
btn_login.place(x=130, y=240)
btn_sign_up = tk.Button(window, text='sign up', command=user_sign_up)
btn_sign_up.place(x=230, y=240)

window.mainloop()
