import tkinter as tk
import tkinter.messagebox
import pickle

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
        return
    try :
        with open('user_info.pickle', 'rb') as user_file :
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle', 'wb') as user_file :
            user_info = {'admin' : 'admin'}  # 写入管理员用户
            pickle.dump(user_info, user_file)
    print(user_info)
    flag = usr_name in user_info
    if flag:
        if usr_pwd == user_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='hello, 你好, ' + usr_name)
        else:
            tk.messagebox.showerror(title='Error', message='passwd is not correct, try again!!!')
    else:
        is_sign_up = tk.messagebox.askyesno(title='sign up?', message='you are not member, do you want to sign up now?')
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    print('sign up')

    def do_sign_up():  # 闭包
        name = new_name.get()
        pwd = new_pwd.get()
        con_pwd = new_confirm_pwd.get()
        print(name, pwd, con_pwd)  # 打印下试试

        if name == '' or pwd == '' or con_pwd == '':
            tk.messagebox.showerror(title='param error', message='must input name, pwd, con_pwd')
            return
        if pwd != con_pwd:
            tk.messagebox.showerror(title='pwd error', message='pwd must eqaul con_pwd')
            return

        try:
            with open('user_info.pickle', 'rb') as usr_file:
                user_info = pickle.load(usr_file)
        except FileNotFoundError :
            with open('user_info.pickle', 'wb') as usr_file:
                user_info = {'admin': 'admin'}
                pickle.dump(user_info, usr_file)

        if name in user_info:
            tk.messagebox.showwarning(title='already exists..', message='you are already is member.')
            win_sign_up.destroy()
        else :
            user_info[name] = pwd  # 这个太方便了
            usr_file = open('user_info.pickle', 'wb')  # 需要重新打开，不然会报io.IoException write不支持写
            pickle.dump(user_info, usr_file)
            tk.messagebox.showinfo(title='Success', message='good luck, you sign up succefully')
            win_sign_up.destroy()

    win_sign_up = tk.Toplevel(window)  # 打开上层窗口
    win_sign_up.title()
    win_sign_up.geometry('350x200')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(win_sign_up, text='new user name : ').place(x=10, y=10)
    entry_new_name = tk.Entry(win_sign_up, textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_pwd = tk.StringVar()
    tk.Label(win_sign_up, text="password : ").place(x=10, y=50)
    entry_new_pwd = tk.Entry(win_sign_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)

    new_confirm_pwd = tk.StringVar()
    tk.Label(win_sign_up, text="confirm password : ").place(x=10, y=90)
    entry_confirm_pwd = tk.Entry(win_sign_up, textvariable=new_confirm_pwd, show='*')
    entry_confirm_pwd.place(x=150, y=90)

    sign_up_btn = tk.Button(win_sign_up, text='sign up now', command=do_sign_up)
    sign_up_btn.place(x=130, y=150)


# login and sign up button
btn_login = tk.Button(window, text='login', command=user_login)
btn_login.place(x=130, y=240)
btn_sign_up = tk.Button(window, text='sign up', command=usr_sign_up)
btn_sign_up.place(x=230, y=240)

window.mainloop()
