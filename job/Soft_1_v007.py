import json
import requests
from functools import partial
from tkinter import *
from tkinter import ttk
def main():
    wm = Tk()
    wm.geometry('1500x750+700+100')
#横向 3Lf
    wm_a1 = LabelFrame(wm,text='打分',width=250,height=50,padx=10, pady=10)
    wm_a2 = LabelFrame(wm,text='选择人员',width=550,height=50,padx=10, pady=10)
    wm_a3 = LabelFrame(wm,text='已选择',width=150,height=600,padx=10, pady=10)
    wm_a4 = LabelFrame(wm,text='已评分.',width=550,height=50,padx=10, pady=10)
    wm_a1.grid(row=0,column=0)
    wm_a2.grid(row=0,column=1)
    wm_a3.grid(row=0,column=2)

    scrollba = Scrollbar(wm_a3)
    scrollba.pack(side=RIGHT, fill=Y)
    wm_a4.grid(row=0,column=3)
#a2,竖向3

    global wm_a2_7
    wm_a2_1 = Frame(wm_a2,width=250,height=50,padx=10, pady=10)
    wm_a2_2 = Frame(wm_a2,width=550,height=50,padx=10, pady=10)
    wm_a2_3 = Frame(wm_a2,width=550,height=50,padx=10, pady=10)
    wm_a2_4 = Frame(wm_a2,width=550,height=50,padx=10, pady=10)
    wm_a2_5 = Frame(wm_a2,width=550,height=50,padx=10, pady=10)
    wm_a2_6 = Frame(wm_a2,width=550,height=50,padx=10, pady=10)
    wm_a2_7 = Frame(wm_a2,width=550,height=50,padx=10, pady=10)
    wm_a2_1.grid(row=1,column=0)
    wm_a2_2.grid(row=2,column=0)
    wm_a2_3.grid(row=3,column=0)
    wm_a2_4.grid(row=4,column=0)
    wm_a2_5.grid(row=5,column=0)
    wm_a2_6.grid(row=6,column=0)
    wm_a2_7.grid(row=7,column=0)
    scrollbar = Scrollbar(wm_a2_7)
    scrollbar.pack(side=RIGHT, fill=Y)
#配置 a1
    # var=StringVar()
    # Entry(root,textvariable=var).pack()
    Label(wm_a1,text="德",).grid(row=0, column=0)
    Label(wm_a1,text="2",).grid(row=1, column=0)
    Label(wm_a1,text="3",).grid(row=2, column=0)
    Label(wm_a1,text="4",).grid(row=3, column=0)
    Label(wm_a1,text="5",).grid(row=4, column=0)
    Label(wm_a1,text="6",).grid(row=5, column=0)
    Label(wm_a1,text="7",).grid(row=6, column=0)
    Label(wm_a1,text="8",).grid(row=7, column=0)
    Label(wm_a1,text="9",).grid(row=8, column=0)
    global var1
    global var2
    global var3
    global var4
    global var5 
    global var6
    global var7
    global var8
    global var9

    global varb_1
    global varb_2
    global varb_3
    global varb_4
    global varb_5
    global varb_6
    global varb_7
    global varb_8
    global varb_9
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()
    var8 = StringVar()
    var9 = StringVar()
    varb_1 = StringVar()
    varb_2 = StringVar()
    varb_3 = StringVar()
    varb_4 = StringVar()
    varb_5 = StringVar()
    varb_6 = StringVar()
    varb_7 = StringVar()
    varb_8 = StringVar()
    varb_9 = StringVar()
    var1.set(15)
    var2.set(15)
    var3.set(15)
    var4.set(15)
    var5.set(15)
    var6.set(15)
    var7.set(15)
    var8.set(15)
    var9.set(15)
    varb_1.set('')
    varb_2.set('')
    varb_3.set('')
    varb_4.set('')
    varb_5.set('')
    varb_6.set('')
    varb_7.set('')
    varb_8.set('')
    varb_9.set('')
    def is_number(s):
        try:
            int(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False
    def btn_test_1(a1,a2,a3,a4,a5,a6,a7,a8,a9):
        varb_1.set('')
        varb_2.set('')
        varb_3.set('')
        varb_4.set('')
        varb_5.set('')
        varb_6.set('')
        varb_7.set('')
        varb_8.set('')
        varb_9.set('')
        a = 0#int
        b = 0#null
        c = 0#not in range
        d = [a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),a9.get()]
        e = []
        f = [15,15,15,5,5,5,15,15,15]
        z = -1
        for i in d:
            z = z+1
            c = z + 1
            # print(int(i))
            print(type(i))
            if is_number(i):
                print(str(c)+'is int')
                e.append(int(i))
            else:
                eval('varb_'+str(c)+'.set("请填写整数")')
                print('var'+str(c)+'.set(f['+str(z)+'])')
                eval('var'+str(c)+'.set(f['+str(z)+'])')
        #f=[] 标准判断
            if int(i)>int(f[z]):

                eval('varb_'+str(c)+'.set("请填写范围内的值")')
                # print('var' + str(z) + '.set(f[' + str(z) + '])')
                eval('var' + str(c) + '.set(f[' + str(z) + '])')


    e_1 = Entry(wm_a1,textvariable=var1, width=5).grid(row=0,column=1)
    e_2 = Entry(wm_a1,textvariable=var2, width=5).grid(row=1,column=1)
    e_3 = Entry(wm_a1,textvariable=var3, width=5).grid(row=2,column=1)
    e_4 = Entry(wm_a1,textvariable=var4, width=5).grid(row=3,column=1)
    e_5 = Entry(wm_a1,textvariable=var5, width=5).grid(row=4,column=1)
    e_6 = Entry(wm_a1,textvariable=var6, width=5).grid(row=5,column=1)
    e_7 = Entry(wm_a1,textvariable=var7, width=5).grid(row=6,column=1)
    e_8 = Entry(wm_a1,textvariable=var8, width=5).grid(row=7,column=1)
    e_9 = Entry(wm_a1,textvariable=var9, width=5).grid(row=8,column=1)
    Label(wm_a1,text="范围(<=15)",).grid(row=0, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=1, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=2, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=3, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=4, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=5, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=6, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=7, column=2)
    Label(wm_a1,text="范围(<=15)",).grid(row=8, column=2)

    Label(wm_a1,textvariable=varb_1, width=5).grid(row=0,column=3)
    Label(wm_a1,textvariable=varb_2, width=5).grid(row=1,column=3)
    Label(wm_a1,textvariable=varb_3, width=5).grid(row=2,column=3)
    Label(wm_a1,textvariable=varb_4, width=5).grid(row=3,column=3)
    Label(wm_a1,textvariable=varb_5, width=5).grid(row=4,column=3)
    Label(wm_a1,textvariable=varb_6, width=5).grid(row=5,column=3)
    Label(wm_a1,textvariable=varb_7, width=5).grid(row=6,column=3)
    Label(wm_a1,textvariable=varb_8, width=5).grid(row=7,column=3)
    Label(wm_a1,textvariable=varb_9, width=5).grid(row=8,column=3)

    btn_1 = Button(wm_a1,text='Button',command=partial(btn_test_1,var1,var2,var3,var4,var5,var6,var7,var8,var9)).grid(row=10,column=0)


    global checklist
    checklist = Text(wm_a2_7, width=20)
    checklist.pack()
    global checklist1
    checklist1 = Text(wm_a3, width=20)
    checklist1.pack()
#配置 a2
    v1 = IntVar()
    # v1.set(3)
    v2 = IntVar()
    global select
    select = []
    def cb_touch(id,ep_id,name,t1,t2):
        print(111)
        c1 = -1
        d = 0
        for i in select:
            c1 = c1+1
            if id == select[c1]['id']:
                d = 1
                select.remove(select[c1])
        if d == 0:
            select.append({'id':id,'ep_id':ep_id,'name':name,'t1':t1,'t2':t2})
            print(select)
        c()

    def c():
        pass
        print(222)
        vars = []
        global checklist1
        checklist1.pack_forget()
        checklist1 = Text(wm_a3, width=20)
        checklist1.pack()
        var = IntVar()
        a = 0
        for i in select:

            checkbutton = Checkbutton(checklist1, text=i["name"], variable=var,
                                      command=partial(cb_touch, i["id"], i["ep_id"], i["name"],
                                                      i["t1"], i["t2"]))
            var.set(0)
            vars.append(var)
            checklist1.window_create("end", window=checkbutton)
            checklist1.insert("end", "\n")
            a=a+1
        checklist1.config(yscrollcommand=scrollba.set)
        scrollba.config(command=checklist1.yview)
        checklist1.configure(state="disabled")
        print(select)

    def a():
        vars = []
        global checklist
        checklist.pack_forget()
        checklist = Text(wm_a2_7, width=20)
        checklist.pack()

        a = v1.get()
        b = v2.get()
        if a == 0 and b == 0:
            res = '[{"id":"1","employ_id":"160","name":"\u5218\u534e\u8425","sex":"1","t_user_1_id":"19","t_user_2_id":"1","now":"2","age":"50","collage":"\u521d\u4e2d","time":"1"},{"id":"3","employ_id":"366","name":"\u8d75\u6653\u5f3a","sex":"1","t_user_1_id":"7","t_user_2_id":"1","now":"1","age":"45","collage":"\u5927\u4e13","time":"1"},{"id":"5","employ_id":"566","name":"\u5510\u6d77","sex":"1","t_user_1_id":"7","t_user_2_id":"1","now":"3","age":"38","collage":"\u672c\u79d1","time":"1"},{"id":"6","employ_id":"586","name":"\u6768\u5175","sex":"1","t_user_1_id":"9","t_user_2_id":"1","now":"1","age":"59","collage":"\u4e2d\u4e13","time":"1"},{"id":"11","employ_id":"924","name":"\u8d75\u529b\u5f3a","sex":"1","t_user_1_id":"12","t_user_2_id":"1","now":"3","age":"54","collage":"\u5927\u4e13","time":"1"},{"id":"13","employ_id":"1054","name":"\u73ed\u51e4\u65fa","sex":"1","t_user_1_id":"12","t_user_2_id":"1","now":"1","age":"57","collage":"\u9ad8\u4e2d","time":"1"},{"id":"18","employ_id":"2057","name":"\u97e9\u741b","sex":"1","t_user_1_id":"7","t_user_2_id":"1","now":"1","age":"30","collage":"\u5927\u4e13","time":"1"},{"id":"21","employ_id":"2278","name":"\u90d1\u5fb7\u798f","sex":"1","t_user_1_id":"20","t_user_2_id":"1","now":"1","age":"33","collage":"\u5927\u4e13","time":"1"},{"id":"22","employ_id":"2372","name":"\u738b\u864e","sex":"1","t_user_1_id":"20","t_user_2_id":"1","now":"1","age":"37","collage":"\u5927\u4e13","time":"1"},{"id":"25","employ_id":"2598","name":"\u66fe\u7eea\u5cf0","sex":"1","t_user_1_id":"14","t_user_2_id":"1","now":"3","age":"30","collage":"\u672c\u79d1","time":"1"},{"id":"34","employ_id":"2690","name":"\u738b\u5764","sex":"1","t_user_1_id":"22","t_user_2_id":"1","now":"1","age":"35","collage":"\u5927\u4e13","time":"1"},{"id":"39","employ_id":"2840","name":"\u674e\u957f\u57f9","sex":"1","t_user_1_id":"16","t_user_2_id":"1","now":"1","age":"31","collage":"\u672c\u79d1","time":"1"},{"id":"41","employ_id":"2874","name":"\u90dd\u671d\u521a","sex":"1","t_user_1_id":"21","t_user_2_id":"1","now":"1","age":"31","collage":"\u5927\u4e13","time":"1"},{"id":"44","employ_id":"2963","name":"\u6210\u52c7","sex":"1","t_user_1_id":"15","t_user_2_id":"1","now":"2","age":"31","collage":"\u5927\u4e13","time":"1"},{"id":"47","employ_id":"3022","name":"\u80e1\u5b66\u56fd","sex":"1","t_user_1_id":"11","t_user_2_id":"1","now":"1","age":"52","collage":"\u9ad8\u4e2d","time":"1"},{"id":"51","employ_id":"3143","name":"\u5f20\u793c","sex":"1","t_user_1_id":"20","t_user_2_id":"1","now":"1","age":"31","collage":"\u672c\u79d1","time":"1"},{"id":"54","employ_id":"3154","name":"\u90d1\u5149\u7eea","sex":"1","t_user_1_id":"19","t_user_2_id":"1","now":"1","age":"31","collage":"\u5927\u4e13","time":"1"},{"id":"55","employ_id":"3179","name":"\u6b66\u94f6","sex":"1","t_user_1_id":"15","t_user_2_id":"1","now":"1","age":"29","collage":"\u5927\u4e13","time":"1"},{"id":"56","employ_id":"3183","name":"\u674e\u6d32\u6d0b","sex":"1","t_user_1_id":"20","t_user_2_id":"1","now":"1","age":"31","collage":"\u672c\u79d1","time":"1"},{"id":"60","employ_id":"3205","name":"\u738b\u5c71\u5ddd","sex":"1","t_user_1_id":"19","t_user_2_id":"1","now":"2","age":"30","collage":"\u672c\u79d1","time":"1"},{"id":"61","employ_id":"3209","name":"\u5434\u6770\u8d24","sex":"1","t_user_1_id":"11","t_user_2_id":"1","now":"2","age":"31","collage":"\u5927\u4e13","time":"1"},{"id":"62","employ_id":"3221","name":"\u6c88\u5b99","sex":"1","t_user_1_id":"6","t_user_2_id":"1","now":"1","age":"29","collage":"\u5927\u4e13","time":"1"},{"id":"63","employ_id":"3239","name":"\u6768\u6770","sex":"1","t_user_1_id":"19","t_user_2_id":"1","now":"1","age":"31","collage":"\u672c\u79d1","time":"1"}]'
        elif a == 0:
            res = '[{"id":"26","employ_id":"2600","name":"\u6234\u5143\u5764","sex":"0","t_user_1_id":"17","t_user_2_id":"2","now":"2","age":"30","collage":"\u672c\u79d1","time":"1"},{"id":"37","employ_id":"2810","name":"\u5218\u660c\u6770","sex":"1","t_user_1_id":"19","t_user_2_id":"2","now":"2","age":"31","collage":"\u5927\u4e13","time":"1"},{"id":"70","employ_id":"3292","name":"\u90b5\u955c\u6f7c","sex":"0","t_user_1_id":"2","t_user_2_id":"2","now":"2","age":"30","collage":"\u672c\u79d1","time":"1"},{"id":"84","employ_id":"3502","name":"\u8d75\u777f\u6b23","sex":"0","t_user_1_id":"3","t_user_2_id":"2","now":"2","age":"27","collage":"\u672c\u79d1","time":"1"},{"id":"86","employ_id":"3555","name":"\u59dc\u4e39","sex":"0","t_user_1_id":"3","t_user_2_id":"2","now":"6","age":"35","collage":"\u672c\u79d1","time":"1"},{"id":"87","employ_id":"3603","name":"\u66fe\u8389\u96ef","sex":"0","t_user_1_id":"13","t_user_2_id":"2","now":"1","age":"30","collage":"\u672c\u79d1","time":"1"},{"id":"104","employ_id":"3776","name":"\u6768\u6653\u73b2","sex":"0","t_user_1_id":"7","t_user_2_id":"2","now":"1","age":"31","collage":"\u672c\u79d1","time":"1"},{"id":"108","employ_id":"3781","name":"\u6768\u5bb6\u742a","sex":"0","t_user_1_id":"11","t_user_2_id":"2","now":"1","age":"25","collage":"\u5927\u4e13","time":"1"},{"id":"115","employ_id":"3806","name":"\u5434\u6625\u71d5","sex":"0","t_user_1_id":"20","t_user_2_id":"2","now":"1","age":"33","collage":"\u672c\u79d1","time":"1"}]'
        elif b == 0:
            res = '[{"id":"2","employ_id":"172","name":"\u8463\u7ea2","sex":"0","t_user_1_id":"16","t_user_2_id":"5","now":"2","age":"52","collage":"\u5927\u4e13","time":"1"},{"id":"4","employ_id":"535","name":"\u9ec4\u6653\u4e3d","sex":"0","t_user_1_id":"8","t_user_2_id":"5","now":"2","age":"50","collage":"\u5927\u4e13","time":"1"},{"id":"16","employ_id":"1425","name":"\u675c\u6dd1","sex":"0","t_user_1_id":"11","t_user_2_id":"5","now":"3","age":"33","collage":"\u672c\u79d1","time":"1"},{"id":"36","employ_id":"2749","name":"\u5468\u6653\u9523","sex":"0","t_user_1_id":"17","t_user_2_id":"5","now":"2","age":"34","collage":"\u672c\u79d1","time":"1"},{"id":"45","employ_id":"2966","name":"\u675c\u8d85","sex":"0","t_user_1_id":"20","t_user_2_id":"5","now":"2","age":"31","collage":"\u5927\u4e13","time":"1"},{"id":"49","employ_id":"3105","name":"\u9648\u5955","sex":"0","t_user_1_id":"15","t_user_2_id":"5","now":"1","age":"29","collage":"\u672c\u79d1","time":"1"},{"id":"59","employ_id":"3204","name":"\u4f55\u4e3d\u971e","sex":"0","t_user_1_id":"3","t_user_2_id":"5","now":"1","age":"30","collage":"\u672c\u79d1","time":"1"},{"id":"68","employ_id":"3280","name":"\u5510\u7476","sex":"0","t_user_1_id":"2","t_user_2_id":"5","now":"2","age":"29","collage":"\u672c\u79d1","time":"1"}]'
        else:
            res = '[{"id":"20","employ_id":"2228","name":"\u674e\u9f99\u5bcc","sex":"1","t_user_1_id":"10","t_user_2_id":"4","now":"2","age":"34","collage":"\u672c\u79d1","time":"1"},{"id":"24","employ_id":"2575","name":"\u674e\u658c","sex":"1","t_user_1_id":"3","t_user_2_id":"4","now":"2","age":"32","collage":"\u672c\u79d1","time":"1"},{"id":"30","employ_id":"2627","name":"\u5218\u6d27\u4f36","sex":"0","t_user_1_id":"15","t_user_2_id":"4","now":"1","age":"32","collage":"\u5927\u4e13","time":"1"},{"id":"31","employ_id":"2643","name":"\u9676\u4e16\u8d85","sex":"0","t_user_1_id":"17","t_user_2_id":"4","now":"2","age":"31","collage":"\u672c\u79d1","time":"1"},{"id":"33","employ_id":"2683","name":"\u7530\u65ed\u946b","sex":"0","t_user_1_id":"11","t_user_2_id":"4","now":"1","age":"34","collage":"\u672c\u79d1","time":"1"},{"id":"52","employ_id":"3148","name":"\u9093\u6db5\u743c","sex":"0","t_user_1_id":"3","t_user_2_id":"4","now":"2","age":"29","collage":"\u672c\u79d1","time":"1"}]'

        result = json.loads(res)
        # print(result)
        print(len(result))  # good response
        # laber_1_text.set('总数: ' + str(len(result)))
        for i in range(len(result)):
            data_i = result[i]
            # print(data_i)

            d = 0
            for j in select:
                if data_i['id'] == j['id']:
                    print(str(data_i['id']) + ' = ' + str(j['id']))
                    d = 1
                    # str1 = 'checkbutton'+str(i)+'=Checkbutton(checklist, text=i, variable=var,command=partial(cb_touch, data_i["id"], data_i["employ_id"],data_i["name"], data_i["t_user_1_id"],data_i["t_user_1_id"]))'
                    # str2 = 'checkbutton'+str(i)+'.select()'
                    # str3 = 'checklist.window_create("end", window=checkbutton'+str(i)+')'
                    # eval(str1)
                    # eval(str2)
                    # eval(str3)
                    # checkbutton=Checkbutton(checklist, text=data_i["name"], variable=var,command=partial(cb_touch, data_i["id"], data_i["employ_id"],data_i["name"], data_i["t_user_1_id"],data_i["t_user_1_id"]))
                    # print(var.get())
                    # # checkbutton.toggle()
                    # vars.append(var)
                    # checklist.window_create("end", window=checkbutton)
                    var = IntVar()
                    checkbutton = Checkbutton(checklist, text=i, variable=var,command=partial(cb_touch, data_i["id"], data_i["employ_id"],
                                                             data_i["name"], data_i["t_user_1_id"],
                                                             data_i["t_user_1_id"]))
                    var.set(1)
                    checklist.window_create("end", window=checkbutton)
                    checklist.insert("end", "\n")
            if d == 0 :
                var = IntVar()
                checkbutton= Checkbutton(checklist, text=data_i["name"], variable=var,command=partial(cb_touch, data_i["id"], data_i["employ_id"],data_i["name"], data_i["t_user_1_id"],data_i["t_user_1_id"]))
                var.set(0)
                vars.append(var)
                checklist.window_create("end", window=checkbutton)
                checklist.insert("end", "\n")
        checklist.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=checklist.yview)
        checklist.configure(state="disabled")

    button1_ALL=Radiobutton(wm_a2_2, text='全选', variable=v1, value=0, indicatoron=False,command=partial(a))  # indicatoron=0/False 按钮样式
    button1_1 = Radiobutton(wm_a2_2, text='本部', variable=v1, value=6, indicatoron=False,command=partial(a))  # indicatoron=0/False 按钮样式
    button1_2 = Radiobutton(wm_a2_2, text='工程技术类', variable=v1, value=1, indicatoron=False,                            command=partial(a))  # indicatoron=0/False 按钮样式
    button1_3 = Radiobutton(wm_a2_2, text='会计资金类', variable=v1, value=2, indicatoron=False,                            command=partial(a))  # indicatoron=0/False 按钮样式
    button1_4 = Radiobutton(wm_a2_2, text='商务材料类', variable=v1, value=3, indicatoron=False,                            command=partial(a))  # indicatoron=0/False 按钮样式
    button1_5 = Radiobutton(wm_a2_2, text='商务类', variable=v1, value=4, indicatoron=False,                            command=partial(a))  # indicatoron=0/False 按钮样式
    button1_6 = Radiobutton(wm_a2_2, text='综合办', variable=v1, value=5, indicatoron=False,                            command=partial(a))  # indicatoron=0/False 按钮样式

    button1_ALL.pack(side=LEFT, )
    button1_1.pack(side=LEFT, )
    button1_2.pack(side=LEFT, )
    button1_3.pack(side=LEFT, )
    button1_4.pack(side=LEFT, )
    button1_5.pack(side=LEFT, )
    button1_6.pack(side=LEFT, )

    button2_ALL=Radiobutton(wm_a2_3, text='显示全部', variable=v2, value=0, indicatoron=False, command=partial(a))
    button2_1 = Radiobutton(wm_a2_3, text='本部', variable=v1, value=6, indicatoron=False, command=partial(a))
    button2_2 = Radiobutton(wm_a2_3, text='温江公交枢纽', variable=v2, value=2, indicatoron=False, command=partial(a))
    button2_3 = Radiobutton(wm_a2_3, text='成都洺悦府', variable=v2, value=3, indicatoron=False, command=partial(a))
    button2_4 = Radiobutton(wm_a2_3, text='成都洺悦锦园', variable=v2, value=4, indicatoron=False, command=partial(a))
    button2_5 = Radiobutton(wm_a2_3, text='成都洺悦玺', variable=v2, value=5, indicatoron=False, command=partial(a))
    button2_6 = Radiobutton(wm_a2_4, text='重庆洺悦芳华', variable=v2, value=6, indicatoron=False, command=partial(a))
    button2_7 = Radiobutton(wm_a2_4, text='重庆洺悦城', variable=v2, value=7, indicatoron=False, command=partial(a))
    button2_8 = Radiobutton(wm_a2_4, text='重庆公园里', variable=v2, value=8, indicatoron=False, command=partial(a))
    button2_9 = Radiobutton(wm_a2_4, text='重庆泷悦华府', variable=v2, value=9, indicatoron=False, command=partial(a))
    button2_10 = Radiobutton(wm_a2_4, text='重庆洺悦国际', variable=v2, value=10, indicatoron=False, command=partial(a))
    button2_11 = Radiobutton(wm_a2_5, text='武汉统建璟樾府', variable=v2, value=11, indicatoron=False, command=partial(a))
    button2_12 = Radiobutton(wm_a2_5, text='武汉将军路', variable=v2, value=12, indicatoron=False, command=partial(a))
    button2_13 = Radiobutton(wm_a2_5, text='武汉盛世江城', variable=v2, value=13, indicatoron=False, command=partial(a))
    button2_14 = Radiobutton(wm_a2_6, text='标准化', variable=v2, value=14, indicatoron=False, command=partial(a))
    button2_15 = Radiobutton(wm_a2_6, text='简阳项目', variable=v2, value=15, indicatoron=False, command=partial(a))
    button2_16 = Radiobutton(wm_a2_6, text='剑阁项目', variable=v2, value=16, indicatoron=False, command=partial(a))
    button2_17 = Radiobutton(wm_a2_6, text='彭州项目', variable=v2, value=17, indicatoron=False, command=partial(a))
    button2_18 = Radiobutton(wm_a2_6, text='沙湾水电站', variable=v2, value=18, indicatoron=False, command=partial(a))
    button2_19 = Radiobutton(wm_a2_6, text='第四项目', variable=v2, value=19, indicatoron=False, command=partial(a))
    button2_20 = Radiobutton(wm_a2_6, text='中韩创新创业园', variable=v2, value=20, indicatoron=False, command=partial(a))
    button2_21 = Radiobutton(wm_a2_6, text='第四项目', variable=v2, value=21, indicatoron=False, command=partial(a))
    button2_22 = Radiobutton(wm_a2_6, text='中韩创新创业园', variable=v2, value=22, indicatoron=False, command=partial(a))

    button2_ALL.pack(side=LEFT, )
    button2_1.pack(side=LEFT, )
    button2_2.pack(side=LEFT, )
    button2_3.pack(side=LEFT, )
    button2_4.pack(side=LEFT, )

    button2_5.pack(side=LEFT, )
    button2_6.pack(side=LEFT, )
    button2_7.pack(side=LEFT, )
    button2_8.pack(side=LEFT, )
    button2_9.pack(side=LEFT, )

    button2_10.pack(side=LEFT, )
    button2_11.pack(side=LEFT, )
    button2_12.pack(side=LEFT, )
    button2_13.pack(side=LEFT, )
    button2_14.pack(side=LEFT, )
    button2_15.pack(side=LEFT, )
    button2_16.pack(side=LEFT, )
    button2_17.pack(side=LEFT, )
    button2_18.pack(side=LEFT, )
    button2_19.pack(side=LEFT, )
    button2_20.pack(side=LEFT, )
    button2_21.pack(side=LEFT, )
    button2_22.pack(side=LEFT, )

    mainloop()
if __name__ == '__main__':
    main()
