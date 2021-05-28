# coding=utf-8
import numpy as np

us_file_path = "../youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "../youtube_video_data/GB_video_data_numbers.csv"

# unpack 转置
t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.arange(0,24).reshape(4,6)

print(t2)
print("*"*100)
print(t2[t2<10])

t2[t2<10] = 3
print(t2)
