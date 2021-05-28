import requests
from lxml import etree
from hashlib import md5
#封装识别验证码图片的函数
class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        # 更改点一
        self.password = md5(password.encode("utf-8")).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

if __name__ == '__main__':
    url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)
    # 解析验证码图片img中src属性值
    tree = etree.HTML(page_text)
    code_img_src = 'https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    # print(code_img_src)
    img_data = requests.get(url=code_img_src,headers=headers).content
    # print(img_data)
    with open('./code.jpg','wb') as fp:
        fp.write(img_data)
    chaojiying = Chaojiying_Client('1572903465', '123456789zxc', '911583')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('./code.jpg', 'rb').read()
    # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, 1902)['pic_str'])  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
# 调用大码平台的实例程序进行验证码图片识别