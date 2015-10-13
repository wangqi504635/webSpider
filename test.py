__author__ = 'wangqi'
# -*- coding:utf-8 -*-
import re

def testre1():
    prefix_url_re = r'http://www.juzimi.com/ju/\d*'
    url1 = 'http://www.juzimi.com/ju/150768'
    url2 = 'http://www.juzimi.com/ju/150768/'
    if re.findall(prefix_url_re,url1):
        print('url1 find')
    if re.findall(prefix_url_re,url2):
        print('url2 find')

def testre2():
    model = r'aaa\d{4,10}$'
    str1 = 'aaa11111'
    str2 = 'aaaa'
    print(re.match(model,str1).string)
    if re.match(model,str1):
        print('str1 find')
    if re.findall(model,str2):
        print('str1 find')

def teststr():
    str1 = 'http/'
    print(str1[0:-1])

def writefile():
    with  open('sample.txt','at') as f:
        f.write('hello')
        f.write('world')

def readfile():
    with  open('sample.txt','rt') as f:
        for line in f:
            print(line)

writefile()
readfile()
