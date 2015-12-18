__author__ = 'wangqi'
# -*- coding:utf-8 -*-
from commen import *
from time import sleep
from bs4 import *
import re
from urllib.parse import quote


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


def get_all_html(total, base_url):
    cur_page = 0
    url = base_url
    while (cur_page <= total):
        sleep(3)
        html = getHtml_proxy(url, proxy_ip)
        write_jz(html)
        cur_page += 1
        url = base_url + "?page=" + str(cur_page)


def get_page_num(url):
    span_re = '.*<span class="xqreplynumhidmax">(.*)</span>跳到'
    html = getHtml_proxy(url, proxy_ip)
    span = re.findall(span_re, html)
    if len(span) == 0:
        return 0
    return int(span.pop())


pre_url = 'http://www.juzimi.com/writer/'
proxy_ip = '120.195.207.99'
page_num = 0
data_re = '\'text\':\'(.*)\',\'desc\''
filename = "writer.txt"
writes = ['戴望舒']
for item in writes:
    filename = item + '.txt'
    base_url = pre_url + quote(item)
    page_num = get_page_num(base_url)
    get_all_html(page_num, base_url)
