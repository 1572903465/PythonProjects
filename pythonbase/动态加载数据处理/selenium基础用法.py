from selenium import webdriver
from lxml import etree
import time
#实例化一个浏览器对象 （传入浏览器的驱动程序）
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
#让浏览器发起一个指定url对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk')

#page_source获取浏览器当前页面的页面源码数据
page_text = bro.page_source
# print(page_text)

#解析企业名称
tree  = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
# print(li_list)
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
time.sleep(5)
bro.quit()