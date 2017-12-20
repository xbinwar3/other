#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver


phantomjs = 'd://phantomjs//bin//phantomjs.exe'

drvJs = webdriver.PhantomJS(executable_path=phantomjs)

drvJs.get("https://www.test.com")
print unicode('fetchURL','utf-8')
#data = drvJs.title
filename = "test_screenshot.png"
print unicode('保存文件','utf-8')
drvJs.save_screenshot(filename)
