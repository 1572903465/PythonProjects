import re

def main01():
    names = ["name1","_name","2_name","__name__","_name#"]

    for name in names:
        result = re.match("^[a-zA-Z_][a-zA-Z0-9_]*$",name)
        if result:
            print("变量名%s符合要求"%result.group())
        else:
            print("变量名%s非法" % name)

if __name__ == '__main__':
    main01()