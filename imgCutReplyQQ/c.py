#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
# 原理是先将需要发送的文本放到剪贴板中，然后将剪贴板内容发送到qq窗口
# 之后模拟按键发送enter键发送消息

import os,time
import win32gui,win32api
import win32con
import win32clipboard as w
from selenium import webdriver
from ctypes import *  

fdir = win32gui.FindWindow(None, 'pycode')
print unicode('图片窗口:'+str(fdir),'utf-8')
win32gui.SetForegroundWindow(fdir)
win32api.keybd_event(17,0,0,0)
win32api.keybd_event(67,0,0,0)  #C键位码是67  
win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0) #释放按键  
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
