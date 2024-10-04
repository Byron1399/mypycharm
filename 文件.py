import os
import shutil

rootdir = 'C:\\Users\\lll13\\Desktop\\船舶数据\\pics\\JPEGImages'
picttxt_list= os.listdir(rootdir)
pict=[]
for i in range(0,len(picttxt_list)):
    if "." in picttxt_list[i]:
        a,b=picttxt_list[i].split('.')
        pict.append(a)
print(pict)


imageaddress='C:\\Users\\lll13\\Desktop\\船舶数据\\train'
destination_folder = os.path.join(rootdir, 'selected_images')
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

mubiaojpg_list=os.listdir(imageaddress)
print(mubiaojpg_list)
mubiao=[]
mubiao1=[]
for i in range (0,len(mubiaojpg_list)):
    a,b=mubiaojpg_list[i].split(".")
    mubiao.append(a)

for i in range (0,len(mubiao)):
    a=mubiao[i]+".jpg"
    mubiao1.append(a)

for i in range(0,len(mubiao)):
    if mubiao[i] in pict:
        path=os.path.join(rootdir,mubiao1[i])
        shutil.move(path,destination_folder)
    else:
        continue