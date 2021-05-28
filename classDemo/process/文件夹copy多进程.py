import multiprocessing
import os,time,random

def copy(queue,file_name,old_folder_name,new_folder_name):
    f_read = open(old_folder_name+"/"+file_name,"rb")
    #print(f_read.read())
    f_write = open(new_folder_name+"/"+file_name,"wb")
    time.sleep(0.1)
    content = f_read.read()
    print(content)
    f_write.write(content)

    f_read.close()
    f_write.close()
    queue.put(file_name)

# def copy_file(file_name,old_folder_name,new_floder_name):
#     print("%s"%file_name)
#     old_f = open(old_folder_name+"/"+file_name,"rb")
#     content = old_f.read()
#     print(content)
#     old_f.close()
#     new_f = open(new_floder_name+"/"+file_name,"wb")
#     new_f.write(content)
#     print("%s复制完成"%file_name)
#     new_f.close()

def main():
    old_folder_name = input("请输入要copy的文件夹的文字：")

    try:
        new_folder_name = old_folder_name+"复件"
        os.mkdir(new_folder_name) #创建一个新的文件夹
    except:
        pass
    file_names = os.listdir(old_folder_name)
    print(file_names)

    po = multiprocessing.Pool(5)

    q = multiprocessing.Manager().Queue()

    for file_name in file_names:
        po.apply_async(copy,(q,file_name,old_folder_name,new_folder_name))
        print("copy:",file_name)
        #po.apply_async(copy_file,(file_name,old_folder_name,new_folder_name))

    po.close()
    po.join()
    all_file_num= len(file_names)
    copy_num = 0;
    while True:
        file_name = q.get()
        time.sleep(0.2)
        copy_num+=1
        print("\r拷贝的进度：%.2f%%"%(copy_num*100/all_file_num),end="")

if __name__ == '__main__':
    main()