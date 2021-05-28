from aip import AipSpeech
import re

position = ["一","二","三","四","五","六","七","八","九","十","11","12","13","14","15"]
class YuyinShibie:
    def __init__(self):
        # 申请百度语音识别
        APP_ID = '24172253'
        API_KEY = '2V7H6pwSBYZ9mD9V7yru1esu'
        SECRET_KEY = 'tOQTa0zmHdOF2YZTajGp5j63tcPWaTQP'

        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 读取文件
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def recognition_file(self):
    # 识别本地文件
        path = 'D:\\file.wav'
        test1 = self.client.asr(self.get_file_content(path), 'wav', 16000, {'dev_pid': 1537, })
        try:
            # print(test1["result"][0])
            if test1["result"][0]:
                return 1,test1["result"][0]
            else:
                return 0, ""
        except Exception:
            return 0,""

    def analyze_file(self):
        count,str_yuying = self.recognition_file()
        chess_position = []
        if count:
            print(str_yuying)
            for line, i in enumerate(str_yuying):
                # print(i,line)
                if line<len(str_yuying)-1:
                    # 棋子的横纵位置在十到十五之间
                    if i+str_yuying[line+1] in position:
                        # print(i+str_yuying[str_yuying.index(i)+1]+1)
                        # c = str_yuying.index(i)
                        # b = i+str_yuying[line+1]
                        # print("---",b)
                        chess_position.append(position.index(i+str_yuying[line+1])+1)
                        if len(chess_position) >= 2:
                            # 棋子位置横纵位置已填满
                            break
                    else :
                        # 棋子的横纵位置在一到九之间
                        if i in position:
                            # print(i,position.index(i)+1)
                            chess_position.append(position.index(i)+1)
                            if len(chess_position) >= 2:
                                # 棋子位置横纵位置已填满
                                break
                # print(chess_position)
            if len(chess_position) == 2:
                # 棋子位置横纵位置已填满,1代表合法数据
                print(chess_position)
                return 1,chess_position
            else:
                return 0,chess_position

if __name__ == '__main__':
    yuying = YuyinShibie()
    # yuying.recognition_file()
    yuying.analyze_file()


