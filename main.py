__author__ = 'wangqi'
import re
from commen import getHtml
# -*- coding:utf-8 -*-

page = 1
initail_url = 'http://www.qiushibaike.com/hot/page/' + str(page)

html = getHtml(initail_url)
pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern,html)
for item in items:
     haveImg = re.search("img",item[3])
     if not haveImg:
        print(item[0],item[1],item[2],item[4])


