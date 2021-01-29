# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/10/27 0027 上午 10:16
# Tool ：PyCharm

import tkinter as tk
import  tkinter.messagebox
import  pickle
import my_icon


class tk_login():

    user_data_file='./dat/usr.dat'

    def create_window(self, toplevel=False,title='main', size=(400, 300), resizable=False):

        if toplevel == False:
            window = tk.Tk()
        else:
            window=tk.Toplevel()

        window.title(title)

        my_icon.set_icon(window,my_icon.USER_ICON)

        if resizable == False:
            window.resizable(False, False)
        else:
            window.resizable(True, True)

        curWidth, curHight = size

        curWidth = int(curWidth)
        curHight = int(curHight)

        scn_w, scn_h = window.maxsize()

        if curWidth >= scn_w:
            curWidth = scn_w

        if curHight >= scn_h:
            curHight = scn_h


        cen_x = (scn_w - curWidth) / 2

        cen_y = (scn_h - curHight) / 2

        size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)

        window.geometry(size_xy)

        return window

    def __init__(self,my_func=None):

        self.my_func=my_func

        self.main_window=self.create_window(title='现场可视化管理平台',size=(400,300),resizable=False)
        my_icon.set_icon(self.main_window,my_icon.USER_ICON)

        self.main_window.attributes("-alpha", 0.9)

        tk.Label(self.main_window, text='账户：').place(x=100, y=100)
        tk.Label(self.main_window, text='密码：').place(x=100, y=140)

        self.var_usr_name = tk.StringVar()
        self.enter_usr_name = tk.Entry(self.main_window, textvariable=self.var_usr_name)
        self.enter_usr_name.place(x=160, y=100)

        self.var_usr_pwd = tk.StringVar()
        self.enter_usr_pwd = tk.Entry(self.main_window, textvariable=self.var_usr_pwd, show='*')
        self.enter_usr_pwd.place(x=160, y=140)

        self.bt_login = tk.Button(self.main_window, text='登录', command=self.check)
        self.bt_login.place(x=120, y=230)
        self.main_window.bind('<Return>',self.on_press_enter)



        self.bt_modify = tk.Button(self.main_window, text='修改密码', command=self.usr_pwd_modify)
        self.bt_modify.place(x=180, y=230)

        self.bt_logquit = tk.Button(self.main_window, text='退出', command=self.usr_sign_quit)
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
               # tk.messagebox.showinfo(title='Welcome', message='用户: '+usr_name+'   登陆成功')
                self.usr_sign_quit()
                if self.my_func==None:
                    pass
                if callable(self.my_func):
                    self.my_func()
                    exit()
                return True
            else:
                tk.messagebox.showerror(message='USERNAME or PASSWORD ERROR!')
                return False

        else:
            tk.messagebox.showerror(message='USERNAME or PASSWORD ERROR!')
            return False

    def usr_sign_quit(self):
        self.main_window.destroy()

    def usr_pwd_modify(self):
        def signtowcg():
            Musername = modify_name.get()
            OldPwd=old_pwd.get()
            NewPwd = new_pwd.get()
            ConfirPwd = pwd_comfirm.get()
            print(Musername,OldPwd,NewPwd, ConfirPwd)
            try:
                with open(self.user_data_file, 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
            except FileNotFoundError:
                tk.messagebox.showerror(message='no user data file, please click 登陆 first')
                return False

            if Musername=='' or OldPwd=='' or NewPwd=='' or ConfirPwd=='':
                tk.messagebox.showerror(message='input all entry')
                return False

            if NewPwd!=ConfirPwd:
                tk.messagebox.showerror(message='new psw and pwd confirm not same')
                return False

            if NewPwd=='admin':
                tk.messagebox.showerror(message='"admin" can not be use as password')
                return False

            if len(NewPwd)<=5:
                tk.messagebox.showerror(message='password must be greater than 6 characters')
                return False

            if Musername  not in exist_usr_info:
                tk.messagebox.showerror(message='用户名不存在！')
                return False

            if exist_usr_info[Musername]!=OldPwd:
                tk.messagebox.showerror(message='原密码不对')
                return False

            if exist_usr_info[Musername]==OldPwd:
                exist_usr_info[Musername] = NewPwd

            try:
                with open(self.user_data_file, 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo(title='成功',message='修改成功')
                on_exit()
                return True
            except Exception as e:
                return False

        def on_exit():
            modidy_user_psw_window.destroy()
            self.main_window.update()
            self.main_window.deiconify()


        self.main_window.withdraw()
        modidy_user_psw_window = self.create_window(title='修改密码',size=(400,300),toplevel=True,resizable=False)

        modify_name = tk.StringVar()
        old_pwd=  tk.StringVar()
        new_pwd = tk.StringVar()
        pwd_comfirm = tk.StringVar()

        modidy_user_psw_window.protocol('WM_DELETE_WINDOW', on_exit)


        tk.Label(modidy_user_psw_window, text='用户名：').place(x=90,y=50)
        tk.Entry(modidy_user_psw_window, textvariable=modify_name).place(x=160, y=50)

        tk.Label(modidy_user_psw_window, text='原密码：').place(x=90,y=100)
        tk.Entry(modidy_user_psw_window, textvariable=old_pwd, show='*').place(x=160, y=100)

        tk.Label(modidy_user_psw_window, text='新密码：').place(x=90,y=150)
        tk.Entry(modidy_user_psw_window, textvariable=new_pwd, show='*').place(x=160, y=150)

        tk.Label(modidy_user_psw_window, text='确认密码：').place(x=90, y=200)
        tk.Entry(modidy_user_psw_window, textvariable=pwd_comfirm, show='*').place(x=160, y=200)
    #确认注册
        bt_confirm = tk.Button(modidy_user_psw_window, text='确定', command=signtowcg).place(x=180,y=240)

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
        window_sign_up = tk.Toplevel(self.main_window)
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

    def on_press_enter(self,event):
        print('1111')
        self.bt_login.focus_get()
        self.check()

    def __del__(self):
        self.main_window.quit()

if __name__ == '__main__':

    def start():
         print(1)

         # app=app16开发版.my_app()
         # app.root.mainloop()

    login=tk_login(my_func=start)
    login.main_window.mainloop()

              
