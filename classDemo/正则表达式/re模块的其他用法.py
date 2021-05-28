import re

def main_01():
    result = re.search(r"\d+","阅读数量为 9999")
    print(result)
    if result:
        print(result.group())

def main_02():
    result = re.findall(r"\d+","python=99，c=655,c++=655")
    print(result)
    # if result:
    #     print(result.group())

if __name__ == '__main__':
    main_01()
    main_02()