import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("goban\\")+len("goban\\")]  # 获取myProject，也就是项目的根路径
dataPath = os.path.abspath(rootPath + 'data\\train.csv') # 获取tran.csv文件的路径
print(curPath , rootPath)