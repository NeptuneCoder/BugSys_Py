#/usr/bin/python
# _*_ coding: UTF-8 _*_
import time
import datetime
import os
def autoPull(n):
    while True:
        print("----------------------------------------")
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "8:21":
            print("shijiandaole....")
            pullFile()
        else:
            print("auto pull file ,current time = %s"%currTime)
        #getPackageName()
    

#timer(10)

def pullErrFile(time,packageName,fileName):
    line = "aws s3 sync s3://sdk-crash-1/%s/%s   %s"%(time,packageName,fileName)
    print(line)
    os.system(line)

#pullErrFile('2017-7-22')

def generateFileName(packagename,time):
    return "%s__%s"%(packagename,time)

def generateTime():
    last_date = datetime.date.today()
    return last_date.strftime("%Y-%-m-%-d")
#print(generateFileName("test"))

def pullFile():
    packages = set(['photo.studio.editor.selfie.camera','com.yiba.baidu.wifi','com.xvideostudio.videoeditorlite','com.necta.wifimousefree','com.infreewifi.cct','com.dianxinos.dxbs','com.yiba.sdk', 'com.yiba.sharewe.lite.activity', 'com.baidu.app', 'com.yiba.baidu.wifi'])
    for name in packages:
        print("name = %s"%name)
        #pullErrFile(generateTime(),name,generateFileName(name,generateTime()))
        pullErrFile("2017-8-16",name,generateFileName(name,"2017-8-16"))

pullFile()
#autoPull(60)
print(generateTime())
