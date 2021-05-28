import re

def add(temp):
    strNum = temp.group()
    num = int(strNum)+1
    return str(strNum)

ret = re.search(r"\d+","python = 997")
result1 = re.sub(r"\d+",add(ret),"python = 997")
print(result1)

ret2 = re.search(r"\d+","python = 99")
result2 = re.sub(r"\d+","999","python=99")
print(result2)