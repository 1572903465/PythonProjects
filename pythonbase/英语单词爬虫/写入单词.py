def writer_word(input_data,read_data):
    for i in range(len(read_data)):
        if input_data == read_data[i].strip():
            print("该单词已经存在了,%s在第%d行"%(input_data,i+1))
            return
    file.write(input_data + '\n')

def check_word(input_data,data):
    print(len(data))
    for i in range(len(data)):
        if input_data == data[i].strip():
            print(data[i].strip())
            return

if __name__ == '__main__':
    while True:
        file = open(r'C:\Users\weiwei\Desktop\word\word.txt','a+',encoding='utf-8')
        input_data = input("请输入单词:\n")
        if input_data:
            file.seek(0)      #readlines()是从当前光标的位置开始读取，file.seek(0)将光标移到第一行
            read_data = file.readlines()
            writer_word(input_data,read_data)
            check_word(input_data,read_data)
        else:
            print('请不要输入空字符')
        file.close()

