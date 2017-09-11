#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import os
import pymysql
import time
def parseFile():
    try:
        path = "bugFlags.txt"

        iter_f = iter(open(path))
        for line in iter_f:
            updateBugInfo(line)
            print(line)
    except Exception as e:
        print("has an exception= %s"%e)

def updateBugInfo(bugFlag):
    # get db obj
    db = pymysql.connect("localhost","root","root","bugDB")
    cursor = db.cursor()
    try:
        print(bugFlag)
        bugFlag = str(bugFlag.strip('\n'))
        sql ="update bugInfo set bug_status = 'fix' where bug_detail like '%%%s%%'"%bugFlag       
        row =  cursor.execute(sql)
        print("row = "+ str(row))
        db.commit()
        print('update successed')
    except Exception as e:
        db.rollback()
        print('update failed',e)
    db.close()

def autoUpdate(n):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "22:30":
            parseFile()

autoUpdate(60)
