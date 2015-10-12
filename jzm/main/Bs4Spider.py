__author__ = 'wangqi'
# -*- coding:utf-8 -*-
import urllib.request
import re
import queue
from bs4 import BeautifulSoup

# url = "http://www.juzimi.com/"
inital_url = "http://www.juzimi.com/ju/55412"
prefix_url = "http://www.juzimi.com/ju/"

content_re = ".*句子欣赏评论: “(.*)” 原作者：.*"
author_re = ".*原作者：(.*)出处：出自.*"
book_re = ".*出处：出自《(.*)》.*"

url_queue = queue.Queue(-1)
seen=set()





def getHtml(url):
    try:
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        response = opener.open(url)
        html = response.read()
        html = html.decode('utf-8')
        return html
    except Exception as err:
        print(err)
        return '<html/>'


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

def extract_urls(html,url_base):
    soup = BeautifulSoup(html,"lxml")
    for a in soup.find_all('a'):
        if 'href' in a.attrs:
            if 'http' in a['href']:
                yield a['href']
            elif '/' in a['href']:
                yield url_base + a['href']

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

if __name__ == '__main__':
   main()

