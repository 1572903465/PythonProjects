import re

def main_01():
    result = re.match(r"速度与激情\w","速度与激情E")
    print(result)
    if result:
        print(result.group())

def main_02():
    result = re.match(r"速度与激情\w","速度与激情e")
    print(result)
    if result:
        print(result.group())

def main_03():
    result = re.match(r"速度与激情\w","速度与激情3")
    print(result)
    if result:
        print(result.group())

def main_04():
    result = re.match(r"速度与激情\w","速度与激情_")
    print(result)
    if result:
        print(result.group())

def main_05():
    result = re.match(r"速度与激情\s\w","速度与激情\t_")
    print(result)
    if result:
        print(result.group())

def main_06():
    result = re.match(r"速度与激情.","速度与激情a")
    print(result)
    if result:
        print(result.group())

def main_07():
    result = re.match(r"....","速度与激情a")
    print(result)
    if result:
        print(result.group())


if __name__ == '__main__':
    main_01()
    main_02()
    main_03()
    main_04()
    main_05()
    main_06()
    main_07()