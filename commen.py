__author__ = 'wangqi'

import urllib
from urllib import request
from bs4 import BeautifulSoup


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
            print(err)
        return '<html/>'

def getHtml2(url):
    try:
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        proxy_handler = urllib.request.ProxyHandler({"http" : 'http://120.195.203.219:80'})
        opener = urllib.request.build_opener(proxy_handler)
        # opener = request.build_opener()
        opener.addheaders = [headers]
        response = opener.open(url)
        html = response.read()
        html = html.decode('utf-8')
        return html
    except Exception as err:
        if(__name__ == '__main__'):
            print(err)
        return '<html/>'



def extract_urls(html, url_base):
    soup = BeautifulSoup(html, "lxml")
    for a in soup.find_all('a'):
        if 'href' in a.attrs:
            if 'http' in a['href']:
                yield a['href']
            elif '/' in a['href']:
                yield url_base + a['href']

if __name__ == '__main__':
   url = 'http://www.juzimi.com'
   print(getHtml2(url))
