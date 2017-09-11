#!/usr/bin/python
# -*- coding: UTF-8 -*-

import insertUtils
import time
import Common


def autoInsert(n):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        #if currTime == "22:00":
        print ("shijiandaole....", Common.generateTime())
        insertUtils.parseFile("",Common.generateTime())
        #else:
        print("test ...%s"%currTime)