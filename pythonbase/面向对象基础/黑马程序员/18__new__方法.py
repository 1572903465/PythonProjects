class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
    #     1.创键对象时，new方法会被自动调用
        print("创键对象，分配空间")

    #     2. 为对象分配空间
        instance = super().__new__(cls)
    #     3. 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")

# 创键播放器对象
Player = MusicPlayer()

print(Player)