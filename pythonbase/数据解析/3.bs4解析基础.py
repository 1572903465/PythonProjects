from bs4 import BeautifulSoup
if __name__ == '__main__':
    #將本地的html文档中的数据加载到该对象中
    fp = open('./四川师范大学.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup.a)  # soup.tagName:返回的是文档中第一次出现的tagName 标签
    # print(soup.div)  # soup.tagName:返回的是html中第一次出现的tagName 标签
    # print(soup.find('a')) # find('tagName'): 等同于soup.tagName
    # print(soup.find('div',class_= 'container'))
    # print(soup.find_all('a')) #find_all() 返回值为列表
    # print(soup.select('#navbar'))
    # print(soup.select('#navbar > ul >li')[0])
    print(soup.select('#navbar > ul a')[1].string)
    print(soup.select('#navbar > ul a')[0]['href'])