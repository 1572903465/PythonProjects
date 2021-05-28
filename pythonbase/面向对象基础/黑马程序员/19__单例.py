class MusicPlayer(object):
    # 记录第一个被创建对象的应用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象,cls就是当前类的对象，instance是类属性
        if cls.instance is None:
            # 2. 调 用父类的方法，为第一个对象分配空间，后续的对象都引用同一个空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象应用
        return cls.instance

    def __init__(self):
        print("初始化播放器")

# 创键多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)