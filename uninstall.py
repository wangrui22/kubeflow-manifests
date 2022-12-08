#!/bin/python
#coding:utf-8
import os
import subprocess
import sys
import time

def uninstall(path):
    for root,path,files in os.walk(path):
        files = sorted(files)
        for f in files:
            installfile = root + "/" + f
            cmd = "kubectl delete -f {installfile}".format(installfile=installfile)
            print(cmd)
            p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            out = p.stdout.read()
            print(out)
            #time.sleep(10)

'''
因为一些patch安装涉及到的一些修改需要重启pod，所以先删除再安装
'''
def patchUninstall(path):
    print("start to patch...")
    for root,path,files in os.walk(path):
        files = sorted(files)
        for f in files:
            installfile = root + "/" + f
            cmd_delete = "kubectl delete -f {installfile}".format(installfile=installfile)
            p = subprocess.Popen(cmd_delete,shell=True,stdout=subprocess.PIPE)
            out = p.stdout.read()
            print(out)

# 安装文件
path = "./manifest1.3"
uninstall(path)

# 安装patch
patchPath = "./patch"
patchUninstall(patchPath)