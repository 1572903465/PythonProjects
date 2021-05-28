from aip import AipSpeech

# 申请百度语音识别
APP_ID = '24172253'
API_KEY = '2V7H6pwSBYZ9mD9V7yru1esu'
SECRET_KEY = 'tOQTa0zmHdOF2YZTajGp5j63tcPWaTQP'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别本地文件
path = 'D:\\file.wav'
test1 = client.asr(get_file_content(path), 'wav', 16000, {'dev_pid': 1537, })

print(test1)
print(test1['result'][0])
for i in test1['result'][0]:
    print(i)
