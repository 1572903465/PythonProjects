class Stack(object):
    def __init__(self):
        self.__data = []

    def is_empty(self):
        """判断栈是否为空"""
        return self.__data == []

    def push(self, data):
        """在栈顶添加元素"""
        self.__data.append(data)

    def pop(self):
        """弹出顶部元素"""
        return self.__data.pop()

    def peek(self):
        """返回栈顶元素"""
        # 先判断是否为空
        if self.is_empty():
            return
        else:
            return self.__data[-1]

    def size(self):
        """判断长度"""
        return len(self.__data)

    def travel(self):
        """遍历所有元素"""
        self.__data = self.__data[::-1]
        for i in self.__data:
            print(i)


if __name__ == '__main__':
    a = Stack()
    print(a.is_empty())
    a.push(0)
    a.push(1)
    a.push(2)
    a.push(3)
    a.travel()
