def main():
    file = open(r'C:\Users\weiwei\Desktop\word\word.txt','r',encoding='utf-8')
    #‪C:\Users\weiwei\Desktop\demo1.docx
    a=file.readlines()
    file.close()
    print(len(a))
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]==a[j] and i!=j:
                print("%d=%s"%(i,a[j].strip()))
if __name__ == '__main__':
    main()
