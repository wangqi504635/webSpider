__author__ = 'wangqi'
# -*- coding:utf-8 -*-
from commen import *
import re
import queue
import pymysql
from time import sleep
from kuaidaili import get_ip


url = "http://www.juzimi.com"
prefix_url_content = 'http://www.juzimi.com/ju/\d{1,10}$'
prefix_url_jzm = 'http://www.juzimi.com'
content_re = '.*句子欣赏评论: “(.*)” 原作者：.*'
author_re = '.*原作者：(.*)出处：出自.*'
book_re = '.*出处：出自《(.*)》.*'

url_queue = queue.Queue(-1)
seen=set()

def print_msg(html):
    result = re.findall(content_re,html)
    for juzi in result:
        print(juzi,end=',')
    result = re.findall(author_re,html)
    for juzi in result:
        print(juzi,end=',')
    result = re.findall(book_re,html)
    for juzi in result:
        print(juzi)



def main():
    url_queue.put(url)
    while(True):
        for ip,port in get_ip():
            print(port,ip)
            current_url = url_queue.get(block=False)
            if current_url[-1] == '/':
                current_url = current_url[0:-1]
            html = getHtml_proxy(current_url,'http://' + ip + ':' + port)
            seen.add(current_url)
            if prefix_url_content in current_url:
                print_msg(html)
            for next_url in extract_urls(html,current_url):
                if next_url not in seen and prefix_url_jzm in next_url:
                    url_queue.put(next_url)
            sleep(1)

main()
