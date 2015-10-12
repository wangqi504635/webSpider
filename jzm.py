__author__ = 'wangqi'
# -*- coding:utf-8 -*-
from commen import *
import re
import queue
import pymysql
import time


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
        time.sleep(5)
        current_url = url_queue.get()
        print("current url :", current_url)
        seen.add(current_url)
        html = getHtml(current_url)
        if prefix_url in current_url:
            print_msg(html)
        for next_url in extract_urls(html,current_url):
            if next_url not in seen:
                url_queue.put(next_url)

def init_from_db():
    try:
        conn = pymysql.connect(host='127.0.0.1',port = 3307, user='spider',passwd='spider', db='spider')
        cur = conn.cursor()
        cur.execute("select * from jzm_url_queue")
        r = cur.fetchall()
        for i in r:
            url_queue.put(str(i[0]))
        cur.execute("select * from jzm_url_seen")
        r = cur.fetchall()
        for i in r:
            seen.add(str(i[0]))
        cur.execute("delete * from  jzm_url_seen")
        cur.execute("delete * from  jzm_url_queue")
        conn.commit()
    except Exception as err:
        print(err)

def save_to_db():
    try:
        conn = pymysql.connect(host='127.0.0.1',port = 3307, user='spider',passwd='spider', db='spider')
        cur = conn.cursor()
        for url in seen:
            cur.execute('insert into jzm_url_seen values ('+ url +')')
        while(True):
            try:
                ret = url_queue.get(block=False)
                sql = 'insert into jzm_url_queue (`url`) values (\''+ ret +'\');'
                cur.execute(sql)
            except Exception as err:
                print(err)
                break
        conn.commit()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()

