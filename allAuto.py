#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import Common
import pullFileUtils,updateBugFlagUtils,insertUtils

print("|--------------------------------------------------------|")
print("|------------------------welcome-------------------------|")
print("|--------------------------------------------------------|")

def autoInsert(n):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "22:00":
            pullFileUtils.read_config()
            print ("pull file ....", Common.generateTime())
        elif currTime == "22:30":
            print("insert to db ....")
            insertUtils.mysql_insert(Common.generateTime())
        elif currTime == "23:00":
            print("23:30")
        elif currTime == "23:30":
            updateBugFlagUtils.read_config()
            print("update ... ")

        elif currTime == "23:50":
            print("22:30")
        else:
            print("test ...%s"%currTime)

autoInsert(60)