# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/27 0027 上午 10:16
# Tool ：PyCharm

import tkinter as tk
import  tkinter.messagebox
import  pickle

class tk_login():

    window = tk.Tk()
    window.title('login')
    window.resizable(False, False)
    user_data_file='.//usr_info.dat'



    def set_win_center(self,root, curWidth='', curHight=''):


        if not curWidth:

            curWidth = root.winfo_width()

        if not curHight:

            curHight = root.winfo_height()

        scn_w, scn_h = root.maxsize()

        cen_x = (scn_w - curWidth) / 2

        cen_y = (scn_h - curHight) / 2

        size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)

        root.geometry(size_xy)

    def __init__(self):
        self.set_win_center(self.window,curWidth=400,curHight=300)

        tk.Label(self.window, text='账户：').place(x=100, y=100)
        tk.Label(self.window, text='密码：').place(x=100, y=140)

        self.var_usr_name = tk.StringVar()
        self.enter_usr_name = tk.Entry(self.window, textvariable=self.var_usr_name)
        self.enter_usr_name.place(x=160, y=100)

        self.var_usr_pwd = tk.StringVar()
        self.enter_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, show='*')
        self.enter_usr_pwd.place(x=160, y=140)

        self.bt_login = tk.Button(self.window, text='登录', command=self.check)
        self.bt_login.place(x=120, y=230)

        self.bt_modify = tk.Button(self.window, text='修改密码', command=self.usr_pwd_modify)
        self.bt_modify.place(x=180, y=230)

        self.bt_logquit = tk.Button(self.window, text='退出', command=self.usr_sign_quit)
        self.bt_logquit.place(x=260, y=230)

    def check(self):
        #输入框内容
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        try:
            with open(self.user_data_file, 'rb') as usr_file:
                usrs_info=pickle.load(usr_file)
        except:
            tk.messagebox.showinfo(title='Notice', message='初次登陆或者无用户信息,初始化用户名为:admin,密码为:admin,建议修改使用')
            with open(self.user_data_file, 'wb') as usr_file:
                usrs_info={'admin':'admin'}
                pickle.dump(usrs_info, usr_file)
            return False

        if usr_name == '' or usr_pwd == '':
            tk.messagebox.showerror(message='用户名密码不能为空！')
            return False

        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(title='Welcome', message='用户: '+usr_name+'   登陆成功')
                self.usr_sign_quit()
                return True
            else:
                tk.messagebox.showerror(message='USERNAME or PASSWORD ERROR!')
                return False

    def usr_sign_quit(self):
        self.window.destroy()

    def usr_pwd_modify(self):
        def signtowcg():
            Musername = modify_name.get()
            OldPwd=old_pwd.get()
            NewPwd = new_pwd.get()
            ConfirPwd = pwd_comfirm.get()
            if Musername=='' or OldPwd=='' or NewPwd=='' or ConfirPwd=='':
                tk.messagebox.showerror(message='input all entry')
                return False
            if NewPwd!=ConfirPwd:
                tk.messagebox.showerror(message='new psw and pwd confirm not same')
                return False

            try:
                with open(self.user_data_file, 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
            except FileNotFoundError:
                tk.messagebox.showerror(message='no user data file, please click 登陆 first')
                return  False

            if Musername  not in exist_usr_info:
                tk.messagebox.showerror(message='用户名不存在！')
                return False
            if exist_usr_info[Musername]!=OldPwd:

                tk.messagebox.showerror(message='原密码不对')
                return False

            if exist_usr_info[Musername]==OldPwd:
                exist_usr_info[Musername] = NewPwd

            with open(self.user_data_file, 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo(title='成功',message='修改成功')
            return True

        def on_exit():
            window_modify.destroy()


            self.window.deiconify()
            self.window.update()


        self.window.withdraw()
        window_modify = tk.Toplevel(self.window)

        window_modify.title('修改密码')
        window_modify.resizable(False, False)
        self.set_win_center(window_modify, 400, 300)

        modify_name = tk.StringVar()
        old_pwd=  tk.StringVar()
        new_pwd = tk.StringVar()
        pwd_comfirm = tk.StringVar()

        window_modify.protocol('WM_DELETE_WINDOW', on_exit)


        tk.Label(window_modify, text='用户名：').place(x=90,y=50)
        tk.Entry(window_modify, textvariable=modify_name).place(x=160, y=50)

        tk.Label(window_modify, text='原密码：').place(x=90,y=100)
        tk.Entry(window_modify, textvariable=old_pwd, show='*').place(x=160, y=100)

        tk.Label(window_modify, text='新密码：').place(x=90,y=150)
        tk.Entry(window_modify, textvariable=new_pwd, show='*').place(x=160, y=150)

        tk.Label(window_modify, text='确认密码：').place(x=90, y=200)
        tk.Entry(window_modify, textvariable=pwd_comfirm, show='*').place(x=160, y=200)
    #确认注册
        bt_confirm = tk.Button(window_modify, text='确定', command=signtowcg).place(x=180,y=240)

    def usr_sign_up(self):
        def signtowcg():
            m_user_name = new_name.get()
            NewPwd = new_pwd.get()
            ConfirPwd = pwd_comfirm.get()
            try:
                with open(self.user_data_file, 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
            except FileNotFoundError:
                exist_usr_info = {}
            if m_user_name in exist_usr_info:
                tk.messagebox.showerror(message='用户名存在！')
            elif m_user_name == '' and NewPwd == '':
                tk.messagebox.showerror(message='用户名和密码不能为空！')
            elif NewPwd != ConfirPwd:
                tk.messagebox.showerror(message='密码前后不一致！')
            else:
                exist_usr_info[m_user_name] = NewPwd
                with open(self.user_data_file, 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                    tk.messagebox.showinfo(message='注册成功！')
                    window_sign_up.destroy()

        # 新建注册窗口
        window_sign_up = tk.Toplevel(self.window)
        window_sign_up.geometry('400x300')
        window_sign_up.title('sign_up')

        # 注册编辑框
        new_name = tk.StringVar()
        new_pwd = tk.StringVar()
        pwd_comfirm = tk.StringVar()

        tk.Label(window_sign_up, text='账户名：').place(x=90, y=50)
        tk.Entry(window_sign_up, textvariable=new_name).place(x=160, y=50)

        tk.Label(window_sign_up, text='密码：').place(x=90, y=100)
        tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=160, y=100)

        tk.Label(window_sign_up, text='确认密码：').place(x=90, y=150)
        tk.Entry(window_sign_up, textvariable=pwd_comfirm, show='*').place(x=160, y=150)
        # 确认注册
        bt_confirm = tk.Button(window_sign_up, text='确定', command=signtowcg).place(x=180, y=220)

app=tk_login()
app.window.mainloop()
              
