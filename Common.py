#!/usr/bin/python
# -*- coding: UTF-8 -*-


from random import Random
import os
import datetime

# 生成包的名字
def generateFileName(packagename,time):

    return "%s%s"%(packagename,time)

#生成一个随机数
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str

def deleteFile(path,packageName,time):
    order = "rm -rf %s%s"%(path,generateFileName(packageName,time))
    os.system(order)

def generateTime():
    last_date = datetime.date.today()
    return last_date.strftime("%Y-%-m-%-d")