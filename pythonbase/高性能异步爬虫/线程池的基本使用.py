# import time

# def get_page(str):
#     print("正在下载：",str)
#     time.sleep(2)
#     print('下载成功:',str)
# if __name__ == '__main__':
#
#     name_list = ['xiaozi','aa','bb','cc']
#
#     start_time = time.time()
#
#     for i in range(len(name_list)):
#         get_page(name_list[i])
#
#     end_time = time.time()
#
#     print('%d second'%(end_time-start_time))

import time
from multiprocessing.dummy import Pool

start_time = time.time()
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print('下载成功:',str)
if __name__ == '__main__':
    name_list = ['xiaozi','aa','bb','cc','dd']
    #实例化一个线程池对象
    pool = Pool(2)
    #将列表中每一个李彪元素传递给get_page处理
    pool.map(get_page,name_list)
    end_time = time.time()
    print('%d second'%(end_time-start_time))

