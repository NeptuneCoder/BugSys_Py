#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import os
import pymysql

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
        sql ="update bugInfo set bug_status = 'fix' where bug_detail like '%%%s%%'"%(bugFlag)
        print(sql)        
        row =  cursor.execute(sql)
        print("row = "+ row)
        db.commit()
        print('update successed')
    except Exception as e:
        db.rollback()
        print('update failed',e)
    db.close()

parseFile()
