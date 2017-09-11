#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pullFileUtils
import time

def autoPull(n):
    while True:
        print("----------------------------------------")
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "21:21":
            print("shijiandaole....")
            pullFileUtils.read_config()

autoPull(60)