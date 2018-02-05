#-*- coding:utf-8 -*-

from selenium import webdriver
from urllib.request import urlretrieve
import os
import time
from openpyxl import Workbook


def main():
    wb = Workbook()
    worksheet = wb.create_sheet("datasheet",0)
    ws = wb.get_sheet_by_name("datasheet")

    url = "http://www.sxtzxm.gov.cn/portalopenPublicInformation.do?method=queryExamineAll"
    browser = webdriver.PhantomJS("C:\\Users\\Administrator\\Downloads\\phantomjs-1.9.7-windows\\phantomjs.exe")

    browser.get(url)
    trlist = browser.find_element_by_class_name("index-table").find_elements_by_tag_name("tr")
    trlen = len(list(trlist))-1
    pagenum = browser.find_element("xpath","//div[@class='pageNum']/span[1]")
    pagenum1 = browser.find_element("xpath", "//div[@class='pageNum']/span[2]")

    print(pagenum.text)
    print(pagenum1.text)
    print(trlen)







if __name__ == '__main__':
    main()