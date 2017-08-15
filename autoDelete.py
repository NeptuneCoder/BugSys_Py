#/usr/bin/python
# _*_ coding: UTF-8 _*_
import time
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
deleteDir("2017-8-8")
