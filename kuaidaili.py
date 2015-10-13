__author__ = 'wangqi'
# -*- coding:utf-8 -*-
#抓取快代理的免费ip
import re
from commen import getHtml
from time import sleep
from bs4 import BeautifulSoup

def get_ip():
    page = 1
    base_url = 'http://www.kuaidaili.com/proxylist/'
    while page <= 10:
        url = base_url + str(page)
        data = getHtml(url)
        soup = BeautifulSoup(data,'lxml')
        for tr in soup.find_all('tr'):
            ip = tr.contents[1].string
            port = tr.contents[3].string
            if 'IP' == ip:
                continue
            yield ip,port
        page+=1
        sleep(1)

if __name__ == '__main__':
    for ip,port in get_ip():
        print(ip + ',' + port)

