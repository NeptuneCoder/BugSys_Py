#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
from random import Random
import time
import pymysql
import datetime

print("|--------------------------------------------------------|")
print("|------------------------welcome-------------------------|")
print("|--------------------------------------------------------|")

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str

# insert data to table
def insert(id,user_county,phone_type,sdk_version,android_id,bug_type,bug_detail,bug_count,bug_status,remark,bug_time,app_name,time):
	# get db obj
    db = pymysql.connect("localhost","root","root","bugDB")

    cursor = db.cursor()

    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()
    print("To prepare  insert")

    sql = "INSERT INTO bugInfo VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,user_county,phone_type,sdk_version,android_id,bug_type,bug_detail,bug_count,bug_status,remark,bug_time,app_name,time)
    try:
        cursor.execute(sql)
        db.commit()
        print('insert successed')
    except Exception as e:
        db.rollback()
        print('insert failed',e)
        print(bug_detail)
    db.close()

# insert data to table
def insertAll(id,user_county,phone_type,sdk_version,android_id,bug_type,bug_detail,bug_count,bug_status,remark,bug_time,app_name,time):
        # get db obj
    db = pymysql.connect("localhost","root","root","bugDB")

    cursor = db.cursor()

    cursor.execute("SELECT VERSION()")

    data = cursor.fetchone()
    print("To prepare  insert")

    sql = "INSERT INTO allBug VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,user_county,phone_type,sdk_version,android_id,bug_type,bug_detail,bug_count,bug_status,remark,bug_time,app_name,time)
    try:
        cursor.execute(sql)
        db.commit()
        print('insert successed')
    except Exception as e:
        db.rollback()
        print('insert failed',e)
        print(bug_detail)
    db.close()

#insert('3','usa','hauwei','2.2.1','adbaec321ea32','outofmery','outofmery','23','fixed','remark','100230302','com.yh.xxx')


def parseFile(path,package,type,time):
    try:
        files = os.listdir(path)
        count = 0
        print(type)
        s = []
        for file in files:
            print('deal ....')
            strName = file+""
            res = strName.split('_')
            countryId = res[0]
            phoneType = res[1]
            sdkVersion = res[2]
            deviceId = res[3]
            bugTime  = res[4].split('.')[0]
            count+=1
            bug_type = " "
            if not os.path.isdir(file):
                f = open(path+"/"+file);
                iter_f = iter(f);
                bug_detail = " \n"
                for line in iter_f:
                    bug_detail = bug_detail + line
                if type == "all":
                    bug_detail = bug_detail.replace("\'",'')
                    insertAll(random_str(),countryId,phoneType,sdkVersion,deviceId,bug_type,bug_detail,'','unfix','',bugTime,package,time)
                else:
                    if 'yiba' in bug_detail:
                        bug_detail=bug_detail.replace("\'",'')
                        insert(random_str(),countryId,phoneType,sdkVersion,deviceId,bug_type,bug_detail,'','unfix','',bugTime,package,time)
        print(count)
    except Exception as e:
        print("has an exception= %s"%e)
    

#path = input("please input file path:")
#package = input("please input app name:")
#type = input("please input type:")
#parseFile(path,package,type)



def generateFileName(packagename,time):
    return "%s__%s"%(packagename,time)

def generateTime():
    last_date = datetime.date.today()
    return last_date.strftime("%Y-%-m-%-d")
#print(generateFileName("test"))

def insertToMysql(type,insertTime):
    packages = set(['photo.studio.editor.selfie.camera','com.yiba.baidu.wifi','com.xvideostudio.videoeditorlite','com.necta.wifimousefree','com.infreewifi.cct','com.dianxinos.dxbs','com.yiba.sdk', 'com.yiba.sharewe.lite.activity', 'com.baidu.app', 'com.yiba.baidu.wifi'])
    for name in packages:
        print("name = %s"%name)
        path = "/root/bugManageSystem/%s"%generateFileName(name,insertTime)
        #path = "/root/bugManageSystem/%s"%generateFileName(name,insertTime)
        parseFile(path,name,type,insertTime)

#insertToMysql("")


def autoInsert(n,insertTime):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "9:30":
            print("shijiandaole....",insertTime)
            insertToMysql("",insertTime)
        else:
            print("insert to mysql ,current time = %s"%currTime)

#autoInsert(60,generateTime())
res = input("please input time:")
insertToMysql("",res)
