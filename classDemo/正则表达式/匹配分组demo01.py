import  re

def main():
    result= re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$","laowang@163.com")
    print(result)
    if result:
        print(result.group())

def main_01():
    result= re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$","laowang@126.com")
    print(result)
    if result:
        print(result.group())

def main_02():
    result= re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$","laowang@126.com")
    print(result)
    if result:
        print(result.group(1))

def main_02():
    result= re.match(r"([a-zA-Z0-9_]{4,20})@(163|126)\.com$","laowang@126.com")
    print(result)
    if result:
        print(result.group(2))

def main_03():
    result= re.match(r"([a-zA-Z0-9_]{4,20})@(163|126)\.com$","laowang@126.com")
    print(result)
    if result:
        print(result.group(3))

if __name__ == '__main__':
    main()
    main_01()
    main_02()
    main_03()