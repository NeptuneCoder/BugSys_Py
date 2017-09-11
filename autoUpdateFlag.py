#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import updateBugFlag
def autoUpdate(n):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "22:30":
            updateBugFlag.read_config()

autoUpdate(60)