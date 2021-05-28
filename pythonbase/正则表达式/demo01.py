import re

def main():
    result = re.match(r"he(.?*)", "hello world")
    print(result)
    print(result.group())

def main_01():
    result = re.match("itcast","itcast.cn")
    result.group()
def main_02():
    result = re.match(r"[Hh]ello", "Hello world")
    print(result)
    print(result.group())

if __name__ == '__main__':
    main()
    main_01()
    main_02()
