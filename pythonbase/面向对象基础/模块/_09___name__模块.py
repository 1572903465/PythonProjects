# 全局变量、函数、类， 注意：直接执行的代码不少向外界提供的工具


def say_hello():
    print("hello hello , i am say hello")

if __name__ == '__main__':

    print(__name__)

    # 文件被导入时， 能够直接执行的代码不需要被执行
    print("the module was developed xiaoming")