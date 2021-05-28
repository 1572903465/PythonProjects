import re

def main_01():
    result = re.match(r"[A-Z][a-z]*","M")
    print(result)
    if result:
        print(result.group())


def main_02():
    result = re.match(r"[A-Z][a-z]*","MnnM")
    print(result)
    if result:
        print(result.group())

def main_03():
    result = re.match(r"[A-Z][a-z]*","Aabcdef")
    print(result)
    if result:
        print(result.group())


def main_04():
    result = re.match(r"021-?\d{8}", "021-12345678")
    print(result)
    if result:
        print(result.group())

def main_05():
    result = re.match(r"\d{3,4}-?\d{7,8}", "0211-1234567")
    print(result)
    if result:
        print(result.group())


if __name__ == '__main__':
    main_01()
    main_02()
    main_03()
    main_04()
    main_05()