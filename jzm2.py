__author__ = 'wangqi'
# -*- coding:utf-8 -*-
import re
import queue
import urllib
from urllib import request
from bs4 import BeautifulSoup
from time import sleep


url = "http://www.juzimi.com"
prefix_url_content = 'http://www.juzimi.com/ju/\d{1,10}$'
prefix_url_jzm = 'http://www.juzimi.com'
content_re = '.*句子欣赏评论: “(.*)” 原作者：.*'
author_re = '.*原作者：(.*)出处：出自.*'
book_re = '.*出处：出自《(.*)》.*'

url_queue = queue.Queue(-1)
seen=set()
f = open('data.txt','at')

def save_msg(html):
    content = re.match(content_re,html).string
    author = re.match(author_re,html).string
    work = re.match(book_re,html).string
    str = content+','+author+','+work+'\n'
    print('write to file>>>>>>>>>>>>>>>>>  :'+str)
    f.write(str)

def trim_url(url):
    if url[-1] == '/':
        url = url[0:-1]
    return url

def getHtml(url):
    try:
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        opener = request.build_opener()
        opener.addheaders = [headers]
        response = opener.open(url)
        html = response.read()
        html = html.decode('utf-8')
        return html
    except Exception as err:
        if(__name__ == '__main__'):
            print('gethtml:'+err)
        return '<html/>'

def getHtml_proxy(url,ip):
    try:
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        if ip is not None:
            proxy_handler = urllib.request.ProxyHandler({"http" : ip})
            opener = urllib.request.build_opener(proxy_handler)
        else:
            opener = request.build_opener()
        opener.addheaders = [headers]
        response = opener.open(url)
        html = response.read()
        html = html.decode('utf-8')
        return html
    except Exception as err:
        if(__name__ == '__main__'):
            print('gethtml proxy:'+err)
        return '<html/>'


def get_ip():
    page = 1
    base_url = 'http://www.kuaidaili.com/proxylist/'
    while page <= 10:
        url = base_url + str(page)
        data = getHtml(url)
        soup = BeautifulSoup(data,'html.parser')
        for tr in soup.find_all('tr'):
            ip = tr.contents[1].string
            port = tr.contents[3].string
            if 'IP' == ip:
                continue
            yield ip,port
        page+=1
        sleep(1)


def extract_urls(html, url_base):
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all('a'):
        if 'href' in a.attrs:
            if 'http' in a['href']:
                yield a['href']
            elif '/' in a['href']:
                yield url_base + a['href'][0:]


def main():
    url_queue.put(url)
    while(True):
        for ip,port in get_ip():
            try:
                current_url = url_queue.get(block=False)
                current_url = trim_url(current_url)
                html = getHtml_proxy(current_url,'http://' + ip + ':' + port)
                print('getting html<<<<<<<<<<<<<<   :' + current_url)
                seen.add(current_url)
                if prefix_url_content in current_url:
                    save_msg(html)
                for next_url in extract_urls(html,current_url):
                    next_url = trim_url(next_url)
                    if prefix_url_jzm not in next_url:
                        seen.add(next_url)
                    if next_url not in seen:
                        url_queue.put(next_url)
                sleep(1)
            except Exception as err:
                print('err xxxxxxxxxx: ' + err)

main()
f.close()
