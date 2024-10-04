import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("wow")
window.geometry("500x500")
lab=tkinter.Label(window,text="wowwww",font=("黑体",12,"bold")).pack()

import pymysql, pandas as pd
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='zjou')
cursor=db.cursor()

def back():
    db.rollback()

def queding():
    db.commit()
def add():
    name=entry1.get()
    num=entry2.get()
    sex=entry3.get()
    sql="insert into student (num,name,sex) values('{0}','{1}','{2}')".format(num,name,sex)
    cursor.execute(sql)

def delete():
    num=entry2.get()
    if values!="":
        x = values[0]
        print(x)
        sql = "delete from student where num='{}'".format(x)
        cursor.execute(sql)
    else :
        sql="delete from student where num='{}'".format(num)
        cursor.execute(sql)


def update():
    name = entry1.get()
    num = entry2.get()
    sex = entry3.get()
    print(name,num,sex)
    sql="update student set name='{0}', sex='{1}' where num='{2}'".format(name,sex,num)
    cursor.execute(sql)





def change():
    def changemima():
        if entry7.get()==entry8.get():
            sql="update teacher set 密码='{}' where 账号='{}' ".format(entry7.get(),z)
            print("dadad",z)
            cursor.execute(sql)
            db.commit()
            changepwdwindow.destroy()
            win_teach.destroy()
        else:
            global wintip
            wintip=tkinter.Tk()
            label1=tkinter.Label(wintip,text="密码不一致").pack()
            button1=tkinter.Button(wintip,text="ok",command=lambda: close(wintip))
            button1.pack()

    changepwdwindow=tkinter.Tk()
    changepwdwindow.title("修改密码")
    changepwdwindow.geometry("500x500")
    label1=tkinter.Label(changepwdwindow,text="密码").pack()
    entry7=tkinter.Entry(changepwdwindow,show='*')
    entry7.pack()
    label2=tkinter.Label(changepwdwindow,text="确认密码").pack()
    entry8=tkinter.Entry(changepwdwindow,show='*')
    entry8.pack()
    button1=tkinter.Button(changepwdwindow,text="修改",command=changemima)
    button1.pack()
def teachpage():
    def on_row_select(event):
        # 获取选中的行
        global values
        selected_item = tree.selection()
        if selected_item:
            item = selected_item[0]
            values = tree.item(item, "values")
            print(type(values))
            print("你选择了行：", values)
        else:
            print("未选择任何行。")
    def shua():
        def update_treeview(df):
            # 清除现有数据
            for item in tree.get_children():
                tree.delete(item)

            # 插入新数据
            for index, row in df.iterrows():
                tree.insert("", "end", values=list(row))

        df = pd.read_sql_query("select * from student", db)
        update_treeview(df)

    global entry1,entry2,entry3,string4,win_teach
    win_teach=tkinter.Tk()
    win_teach.title("教师页面")
    win_teach.geometry("500x500")
    button4 = tkinter.Button(win_teach, text="刷新", command=shua)
    button4.place(x=50,y=110)
    string1=tkinter.Label(win_teach,text="姓名").pack()
    entry1=tkinter.Entry(win_teach)
    entry1.pack()
    string2=tkinter.Label(win_teach,text="学号").pack()
    entry2 = tkinter.Entry(win_teach)
    entry2.pack()
    string3=tkinter.Label(win_teach,text="性别").pack()
    entry3 = tkinter.Entry(win_teach)
    entry3.pack()
    BUTTON1=tkinter.Button(win_teach, text="确定",command=lambda:queding())
    BUTTON1.place(x=50,y=50)
    rollback=tkinter.Button(win_teach, text="撤销",command=lambda:back()).place(x=50,y=80)
    changepwd=tkinter.Button(win_teach, text="修改密码",command=change).place(x=0,y=0)
    button1=tkinter.Button(win_teach,text="增加",command=add).place(x=450,y=50)
    button2=tkinter.Button(win_teach,text="删除",command=delete).place(x=450,y=80)
    button3 = tkinter.Button(win_teach, text="更新", command=update).place(x=450,y=110)
    string4 = tkinter.Label(win_teach)
    string4.pack()
    df = pd.read_sql_query("select * from student", db)
    tree = ttk.Treeview(win_teach, columns=list(df.columns), show='headings')
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    tree.place(x=100,y=250)
    tree.bind("<<TreeviewSelect>>", on_row_select)



def close(a):
    a.destroy()



def teach():

    print(entzh.get())
    global  z
    z=entzh.get()
    print(entp.get())
    df = pd.read_sql_query("select * from teacher", db)
    list=df.values.tolist()
    count=0
    for i in list:
        if i[0]==entzh.get():
            if entp.get() ==i[1]:
                count=1
                teachpage()
                new_window.destroy()
    if count==0:
        global windowteach
        windowteach=tkinter.Tk()
        string=tkinter.Label(windowteach,text="密码或账号错误").pack()
        button1=tkinter.Button(windowteach, text="ok",command=lambda: close(windowteach))
        button1.pack()

def call():
    global entzh,entp,new_window
    new_window = tkinter.Tk()
    new_window.geometry("500x500")
    label1=tkinter.Label(new_window,text="账号").pack()
    entzh=tkinter.Entry(new_window)
    entzh.pack()

    label2=tkinter.Label(new_window,text="密码").pack()
    entp = tkinter.Entry(new_window,show='*')
    entp.pack()
    button3=tkinter.Button(new_window,text="登录",command=teach).pack()

def windowstu():
    def chaxun():
        def update_treeview(df):
            # 清除现有数据
            for item in tree.get_children():
                tree.delete(item)

            # 插入新数据
            for index, row in df.iterrows():
                tree.insert("", "end", values=list(row))


        sql="select * from student where num='{}'".format(quiry.get())
        df=pd.read_sql(sql,db)
        update_treeview(df)


    global quiry
    new_window = tkinter.Tk()
    new_window.geometry("500x500")
    label=tkinter.Label(new_window,text="学号").pack()
    quiry=tkinter.Entry(new_window)
    quiry.pack()
    button1=tkinter.Button(new_window,text="查询",command=lambda:chaxun())
    button1.pack()
    sql = "select * from student "
    df = pd.read_sql(sql,db)
    tree = ttk.Treeview(new_window, columns=list(df.columns), show='headings')
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack()


button = tkinter.Button(window,text="教师登录",font=("黑体",12,"bold"),command=call)
button.place(x=200,y=200)
button2 = tkinter.Button(window,text="学生查询",font=("黑体",12,"bold"),command=windowstu)
button2.place(x=200,y=100)
window.mainloop()
db.close()