__author__ = 'wangqi'
# coding = utf-8


from selenium import webdriver

url = "http://oa:2004/NewOrder.aspx";

browser = webdriver.Firefox()
browser.back()
browser.get(url)
