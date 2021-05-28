import  re

def main():
    email = input("请输入一个邮箱第地址：")
    #匹配字符需要转义
    result= re.match(r"[a-zA-Z0-9_]{4,20}@163\.com$",email)
    if result:
        print("%s符合要求....",email)
    else:
        print("%s不符合要求....",email)

if __name__ == '__main__':
    main()