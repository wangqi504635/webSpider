__author__ = 'wangqi'
# -*- coding:utf-8 -*-
import re
import queue
from commen import *

# url = "http://www.juzimi.com/"
inital_url = "http://www.juzimi.com/ju/55412"
prefix_url = "http://www.juzimi.com/ju/"

content_re = ".*句子欣赏评论: “(.*)” 原作者：.*"
author_re = ".*原作者：(.*)出处：出自.*"
book_re = ".*出处：出自《(.*)》.*"

url_queue = queue.Queue(-1)
seen=set()

def print_msg(html):
    result = re.findall(content_re,html)
    for juzi in result:
        print(juzi)
    result = re.findall(author_re,html)
    for juzi in result:
        print(juzi)
    result = re.findall(book_re,html)
    for juzi in result:
        print(juzi)



def main():
    url_queue.put(inital_url)
    while(True):
        current_url = url_queue.get()
        print("current url :", current_url)
        seen.add(current_url)
        html = getHtml(current_url)
        if prefix_url in current_url:
            print_msg(html)
        for next_url in extract_urls(html,current_url):
            if next_url not in seen:
                url_queue.put(next_url)


html = getHtml(inital_url)
print_msg(html)
