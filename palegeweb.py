from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os

from selenium.webdriver import ActionChains

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver =  webdriver.Chrome(chromedriver)              #用chrome浏览器打开

driver.get("http://manage.sxtzxm.gov.cn/login.do?method=begin")
time.sleep(1)                            #让操作稍微停一下
#找到输入账号的框，并自动输入账号 这里要替换为你的登录账号
driver.find_element_by_id('j_username').send_keys('test')
time.sleep(1)
#密码，这里要替换为你的密码
driver.find_element_by_id('j_password').send_keys('Q!W@e3r4')
time.sleep(1)
#找到登录按钮，并点击
driver.find_element_by_class_name('loginbtn').click()
time.sleep(5)


driver.get("http://manage.sxtzxm.gov.cn/tzxmapp/pages/mianFrame.jsp")
#重新定位页面
time.sleep(2)


driver.switch_to.frame("childmenu")
#切到左侧选择栏frame
time.sleep(2)
driver.find_element_by_id("nimei_1506648496745").click()
time.sleep(2)
driver.find_element_by_link_text("审批事项配置").click()
#进入审批事项配置菜单


driver.switch_to.default_content()
#切回主文档
driver.switch_to.frame("middern")
#切到右侧frame
driver.switch_to.frame("page_1507884981981")
#切到第二层iframe上

driver.get("http://manage.sxtzxm.gov.cn/tzxmapp/controller.do?location=%2Ftzxmapp%2Fpages%2Fconfigure%2FcatalogAndItems%2FitemPowerList_pz.jsp")






