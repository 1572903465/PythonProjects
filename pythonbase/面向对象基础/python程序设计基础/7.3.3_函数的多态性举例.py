def length(x):
    print(repr(x),"of length is",len(x))
    # repr()函数返回一个对象的可输出字符串，无须事前知道是什么类型的。该函数体现了PYthon的多态

if __name__ == '__main__':
    length('aaa')

    length([1,2,3,4,5])