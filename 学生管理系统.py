
import tkinter
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
def add():
    name=entry1.get()
    num=entry2.get()
    sex=entry3.get()
    sql="insert into student (num,name,sex) values('{0}','{1}','{2}')".format(num,name,sex)
    cursor.execute(sql)
    db.commit()

def delete():
    num=entry2.get()
    sql="delete from student where num='{}'".format(num)
    cursor.execute(sql)
    db.commit()

def update():
    name = entry1.get()
    num = entry2.get()
    sex = entry3.get()
    print(name,num,sex)
    sql="update student set name='{0}', sex='{1}' where num='{2}'".format(name,sex,num)
    cursor.execute(sql)
    db.commit()

def teachpage():
    def shua():
        df = pd.read_sql_query("select * from student", db)
        string4.config(text=df.to_string(index=False))
    global entry1,entry2,entry3,string4
    win_teach=tkinter.Tk()
    win_teach.title("教师页面")
    win_teach.geometry("500x500")
    button4 = tkinter.Button(win_teach, text="刷新", command=shua)
    button4.pack()
    string1=tkinter.Label(win_teach,text="姓名").pack()
    entry1=tkinter.Entry(win_teach)
    entry1.pack()
    string2=tkinter.Label(win_teach,text="学号").pack()
    entry2 = tkinter.Entry(win_teach)
    entry2.pack()
    string3=tkinter.Label(win_teach,text="性别").pack()
    entry3 = tkinter.Entry(win_teach)
    entry3.pack()
    button1=tkinter.Button(win_teach,text="增加",command=add).pack()
    button2=tkinter.Button(win_teach,text="删除",command=delete).pack()
    button3 = tkinter.Button(win_teach, text="更新", command=update).pack()
    string4 = tkinter.Label(win_teach)
    string4.pack()







def teach():
    print(entzh.get())
    print(entp.get())
    df = pd.read_sql_query("select * from teacher", db)
    list=df.values.tolist()
    for i in list:
        if i[0]==entzh.get():
            if entp.get() ==i[1]:
                teachpage()
        else:
            windowteach=tkinter.Tk()
            string=tkinter.Label(windowteach,text="error").pack()

def call():
    global entzh,entp
    new_window = tkinter.Tk()
    new_window.geometry("500x500")
    label1=tkinter.Label(new_window,text="账号").pack()
    entzh=tkinter.Entry(new_window)
    entzh.pack()

    label2=tkinter.Label(new_window,text="密码").pack()
    entp = tkinter.Entry(new_window)
    entp.pack()
    button3=tkinter.Button(new_window,text="登录",command=teach).pack()

button = tkinter.Button(window,text="教师登录",font=("黑体",12,"bold"),command=call)
button.pack(padx=100,pady=200)
window.mainloop()