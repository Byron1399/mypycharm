#!/usr/bin/python3

import pymysql
import pandas
import tkinter
from tkinter import ttk

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='zjou')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
df=pandas.read_sql('select * from emp',db)

root=tkinter.Tk()
root.title("www")

tree = ttk.Treeview(root, columns=list(df.columns), show='headings')
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
for index, row in df.iterrows():
    tree.insert("", "end", values=list(row))
tree.pack(fill=tkinter.BOTH, expand=True)

def on_row_select(event):
    # 获取选中的行
    selected_item = tree.selection()
    if selected_item:
        item = selected_item[0]
        values = tree.item(item, "values")
        print(type(values))
        print("你选择了行：", values)
    else:
        print("未选择任何行。")
tree.bind("<<TreeviewSelect>>", on_row_select)
root.mainloop()
