import re

def main():
    result = re.match(r"速度与激情1","速度与激情2")
    print(result)
    if result:
        print(result.group())

def main_01():
    result = re.match(r"速度与激情\d","速度与激情1")
    print(result)
    if result:
        print(result.group())

def main_02():
    result = re.match(r"速度与激情\d","速度与激情5")
    print(result)
    if result:
        print(result.group())

def main_03():
    result = re.match(r"速度与激情\d","速度与激情55")
    print(result)
    if result:
        print(result.group())

def main_04():
    result = re.match(r"速度与激情[1-8]","速度与激情8")
    print(result)
    if result:
        print(result.group())

def main_05():
    result = re.match(r"速度与激情[1-8]","速度与激情8")
    print(result)
    if result:
        print(result.group())

def main_06():
    result = re.match(r"速度与激情[1-8a-z]","速度与激情b")
    print(result)
    if result:
        print(result.group())


if __name__ == '__main__':
    main()
    main_01()
    main_02()
    main_03()
    main_04()
    main_05()
    main_06()