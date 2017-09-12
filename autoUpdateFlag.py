#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import updateBugFlagUtils
def autoUpdate(n):
    while True:
        time.sleep(n)
        currTime = time.strftime("%-H:%-M", time.localtime())
        if currTime == "22:30":
            updateBugFlagUtils.read_config()

autoUpdate(60)