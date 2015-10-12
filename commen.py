__author__ = 'wangqi'

import urllib
from urllib import request
from bs4 import BeautifulSoup


def getHtml(url):
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        # proxy_handler = urllib.request.ProxyHandler({"http" : 'http://4qkueav:4qkueav@korea02.7taomei.com:8001'})
        # opener = urllib.request.build_opener(proxy_handler)
        opener = request.build_opener()
        opener.addheaders = [headers]
        response = opener.open(url)
        html = response.read()
        html = html.decode('utf-8')
        return html


def extract_urls(html, url_base):
    soup = BeautifulSoup(html, "lxml")
    for a in soup.find_all('a'):
        if 'href' in a.attrs:
            if 'http' in a['href']:
                yield a['href']
            elif '/' in a['href']:
                yield url_base + a['href']
