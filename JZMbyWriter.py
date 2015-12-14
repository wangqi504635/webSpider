__author__ = 'wangqi'
# -*- coding:utf-8 -*-
from commen import *
from time import sleep
from bs4 import *
import re

base_url = 'http://www.juzimi.com/writer/%E5%BC%A0%E7%88%B1%E7%8E%B2'
page_num = 66
cur_page = 0
url = base_url
data_re = '\'text\':\'(.*)\',\'desc\''
filename = "writer.txt"


def write_jz(html):
    soup = BeautifulSoup(html, 'lxml')
    for link in soup.find_all('div'):
        if 'id' in link.attrs:
            if link['id'] == 'bdshare':
                result = re.findall(data_re, link['data'])
                for str in result:
                    with  open(filename, 'at', encoding='utf-8') as f:
                        f.write(str)
                        f.write('\n\n')


while (cur_page <= page_num):
    html = getHtml(url)
    write_jz(html)
    cur_page += 1
    url = base_url + "?page=" + str(cur_page)
    sleep(3)
