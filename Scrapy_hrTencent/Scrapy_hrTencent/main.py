# -*- coding:utf-8 -*-
#author:zzy #data:2018/4/24 #Version:Python 3.6
import os,sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy","crawl","tencent"])