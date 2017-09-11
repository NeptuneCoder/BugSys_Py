#!/usr/bin/python
# -*- coding: UTF-8 -*-

import insertUtils
import time
import Common


print("|--------------------------------------------------------|")
print("|------------------------welcome-------------------------|")
print("|--------------------------------------------------------|")

def autoInsert(n):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        #if currTime == "22:00":
        print ("shijiandaole....", Common.generateTime())
        insertUtils.mysql_insert("2017-9-9")
        #else:
        print("test ...%s"%currTime)

autoInsert(10)