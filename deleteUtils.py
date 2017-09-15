#/usr/bin/python
# _*_ coding: UTF-8 _*_

import os

import Common

def deleteDir(time):
    packages = set(['photo.studio.editor.selfie.camera','com.yiba.baidu.wifi','com.xvideostudio.videoeditorlite','com.necta.wifimousefree','com.infreewifi.cct','com.dianxinos.dxbs','com.yiba.sdk', 'com.yiba.sharewe.lite.activity', 'com.baidu.app', 'com.yiba.baidu.wifi'])
    for name in packages:
        print("name = %s"%name)
        order = "rm -rf /root/bugManageSystem/%s"%Common.generateFileName(name,time)
        os.system(order) 
        print(order)
