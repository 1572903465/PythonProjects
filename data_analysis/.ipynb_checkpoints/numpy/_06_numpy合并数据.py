# coding=utf-8
import numpy as np


us_file_path = "../youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "../youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
us_data = np.loadtxt(us_file_path, delimiter=",", dtype="int")
uk_data = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 添加国家信息
# 构造全为0的数据
"""us_data.shape[0]代表us第一位的长度，即行数"""
zeros_data = np.zeros((us_data.shape[0], 1))
ones_data = np.ones((uk_data.shape[0], 1))

# 分别添加一列全为0，1的数据
us_data = np.hstack((us_data,zeros_data)).astype(int)
uk_data = np.hstack((uk_data,ones_data)).astype(int)

# print(us_data)
# print(uk_data)
# 拼接两组数据
final_data = np.vstack((us_data,uk_data))
print(final_data)





