
def writer_word(input_data,a):
    for i in range(len(a)):
        if input_data == a[i].strip():
            print("该单词已经存在了,%s在第%d行"%(input_data,i+1))
            return
    file.write(input_data + '\n')

def check_word(input_data,data):
    print(len(data))
    for i in range(len(data)):
        if input_data == data[i].strip():
            print(data[i].strip())

if __name__ == '__main__':
    while True:
        file = open("demo1.txt","a+")
        input_data = input("请输入单词:\n")
        file.seek(0)
        a = file.readlines()

        writer_word(input_data,a)
        check_word(input_data,a)
        print('a1=', a)
        file.close()

    # fo = open("demo1.txt", "r")
    #
    # print("文件名为: ", fo.name)
    # print("文件列表为: ", fo.readlines())
    # fo.seek(0)
    # for line in fo.readlines():  # 依次读取每行
    #
    #     line = line.strip()  # 去掉每行头尾空白
    #
    #     print("读取的数据为: %s" % (line))
    #
    # # 关闭文件
    #
    # fo.close()


