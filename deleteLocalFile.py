#/usr/bin/python
# _*_ coding: UTF-8 _*_

import datetime

import os

def generateFileName(packagename,time):
    return "%s__%s"%(packagename,time)

def generateTime():
    last_date = datetime.date.today()
    return last_date.strftime("%Y-%-m-%-d")
#print(generateFileName("test"))

def deleteDir(time):
    packages = set(['photo.studio.editor.selfie.camera','com.yiba.baidu.wifi','com.xvideostudio.videoeditorlite','com.necta.wifimousefree','com.infreewifi.cct','com.dianxinos.dxbs','com.yiba.sdk', 'com.yiba.sharewe.lite.activity', 'com.baidu.app', 'com.yiba.baidu.wifi'])
    for name in packages:
        print("name = %s"%name)
        #pullErrFile(time,name,generateFileName(name,time))
        order = "rm -rf /root/bugManageSystem/%s"%generateFileName(name,time)
        os.system(order) 
        print(order)

#deleteDir(generateTime())

def main():
    while True:
        
        time = input("please input time:")
        if (time == "exit"):
            break;
        deleteDir(time)

        os.system("ls")

def deleteFile(type,deleteTime):
    try:
        path = "appNames.txt"
        iter_f = iter(open(path))

        for line in iter_f:
            print("name = %s"%line)
            name = line.strip('\n')
            order = "rm -rf /root/bugManageSystem/%s"%generateFileName(name,deleteTime)
            os.system(order) 

    except Exception as e:
        print("has an exception= %s"%e)

def autoDelete(n):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "23:00":
            print ("shijiandaole....delete file ", genernateTime())
            deleteFile("",generateTime())

autoDelete(60)
