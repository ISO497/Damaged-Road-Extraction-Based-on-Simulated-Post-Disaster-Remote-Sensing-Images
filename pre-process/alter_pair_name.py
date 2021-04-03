import os
from typing import TYPE_CHECKING
path=os.getcwd()

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

n=0
j=1
for i in fileList:
    if (i[-3:]=="jpg"):
        #设置旧文件名（就是路径+文件名）
        oldname_jpg=path+ os.sep + fileList[n]   # os.sep添加系统分隔符
        oldname_png=path+ os.sep + fileList[n].replace("jpg","png")
        #设置新文件名
        newname_jpg=path + os.sep +"original_"+str(j)+".jpg"
        newname_png=path + os.sep +"original_"+str(j)+".png"
        j+=1
        os.rename(oldname_jpg,newname_jpg)   #用os模块中的rename方法对文件改名
        os.rename(oldname_png,newname_png)
    n+=1