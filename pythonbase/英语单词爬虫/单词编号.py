if __name__ == '__main__':
    file = open(r'word.txt', 'r', encoding='utf-8')
    # ‪C:\Users\weiwei\Desktop\demo1.docx
    words = file.readlines()
    file.close()
    # print(words)
    pages=1
    row=46
    count=0
    file = open(r'C:\Users\weiwei\Desktop\word\word1.txt', 'a+', encoding='utf-8')
    for word in words:
        file.write(word)
        print(word)
        count = count+1;
        if count == 25:
            count=0
            numbers=str(pages)+'-'+str(row)+'\n'
            file.write(numbers)
            print(numbers)
            row=row+1
            if row == 50:
                pages=pages+1
                row=0


