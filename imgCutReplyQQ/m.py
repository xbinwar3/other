#!/usr/bin/env python
#coding=utf-8
import os,time
import win32gui,win32api
import win32con
import win32clipboard as w
from selenium import webdriver
from ctypes import *  
def main():
    i = 0
    while 1:
        i += 1
        print unicode('执行-------'+str(i)+'-------次','utf-8')
        print unicode('发消息','utf-8')
        os.system('msg.py')#发消息
        time.sleep(1)
        print unicode('截屏','utf-8')
        os.system('shot.py')#截屏
        time.sleep(1)
        print unicode('copy','utf-8')
        os.system('c.py')#copy
        time.sleep(1)
        print unicode('发图','utf-8')
        os.system('img.py')#发图
        print unicode('END','utf-8')
	time.sleep(120)
if __name__ == "__main__":
#    try: 
#        pid = os.fork() 
#        if pid > 0:
#            sys.exit(0) 
#    except OSError, e: 
#        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
#        sys.exit(1)
#    os.chdir("/") 
#    os.setsid() 
#    os.umask(0) 
#    try: 
#        pid = os.fork() 
#        if pid > 0:
#            print "Daemon PID %d" % pid 
#            sys.exit(0) 
#    except OSError, e: 
#        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
#        sys.exit(1) 
    main() 
