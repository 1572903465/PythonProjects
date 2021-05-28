# 需求爬取糗事百科中糗图模块下的所有图片图片
import requests
if __name__ == '__main__':
    # 如何爬取图片数据
    url = 'https://pic.qiushibaike.com/system/pictures/12371/123715055/medium/BZKZ1TUA3CLHJRWR.jpg'
    # content 返回的是二进制形式的图片数据
    # text（字符串）  content (二进制）  json() (对象）
    img_data = requests.get(url=url).content
    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)