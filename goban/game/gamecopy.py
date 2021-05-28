class Game(object):

    __instance = None
    fiveGroup = []
    points = []

    # def __init__(self):
    #     self.fiveGroup = []

    def init_fiveGroups(self):

        # 纵向的
        for y in range(1, 16):
            for x in range(1, 12):
                self.fiveGroup.append([[x, y], [x + 1, y], [x + 2, y], [x + 3, y], [x + 4, y]])
        # print(1,len(fiveGroup))
        # 横向的
        for x in range(1, 16):
            for y in range(1, 12):
                self.fiveGroup.append([[x, y], [x, y + 1], [x, y + 2], [x, y + 3], [x, y + 4]])
        # print(2,len(fiveGroup))
        #  '/'左半边
        for y in range(5, 16):
            for l in range(1, y - 4):
                self.fiveGroup.append([[l, y], [l + 1, y - 1], [l + 2, y - 2], [l + 3, y - 3], [l + 4, y - 4]])
        # print(3,len(fiveGroup))
        #  '/'右半边
        for x in range(2, 12):
            for l in range(15, x + 2, -1):
                self.fiveGroup.append([[x, l], [x + 1, l - 1], [x + 1, l - 2], [x + 1, l - 3], [x + 1, l - 4]])
        # '\'左部分
        # print(4,len(fiveGroup))
        for x in range(11, 0, -1):
            for l in range(1, 12 - x):
                self.fiveGroup.append([[x, l], [x + 1, l + 1], [x + 1, l + 2], [x + 1, l + 3], [x + 1, l + 4]])
        # '\' 右部分
        # print(5,len(fiveGroup))
        for y in range(2, 12):
            for l in range(1, 13 - y):
                self.fiveGroup.append([[y, l], [y + 1, l + 1], [y + 2, l + 2], [y + 3, l + 3], [y + 4, l + 4]])
        # print(6, len(self.fiveGroup))
        # print(self.fiveGroup)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.init_fiveGroups(cls)
            print("new------------------")
        return cls.__instance

    # 判赢输入最后下棋的棋子坐标(X, Y)与棋子的颜色Z[0, 1], 判断是否获胜
    def CheckWin(self,X,Y,Z): #	X：横坐标； Y：纵坐标； Z：棋子颜色：1为黑、0为白
        max = 0
        tempXIndex = X
        tempYIndex = Y

        # 三维数组记录横向，纵向，左斜，右斜的移动
        dir = [[[-1, 0], [1, 0]], [[0, -1], [0, 1]], [[-1, -1], [1, 1]], [[1, -1], [-1, 1]]] #横向 竖着 左斜 右斜

        for i in range(0,4):
            count = 1
            # j为0, 1分别为棋子的两边方向，比如对于横向的时候，j = 0, 表示下棋位子的左边，j = 1的时候表示右边
            for j in range(0,2):
                flag = True

                while flag:
                    k = 0
                    array = []
                    tempXIndex = tempXIndex + dir[i][j][0]
                    tempYIndex = tempYIndex + dir[i][j][1]
                    # 遍历棋子的位置找到当前棋子的数据
                    for arr in self.points:
                        if arr[0] == tempXIndex and arr[1] == tempYIndex :
                            k = 1
                            array = arr

                    # 棋盘大小的判断 防止越界
                    if tempXIndex >= 1 and tempXIndex <= 15 and tempYIndex >= 1 and tempYIndex <= 15 :
                        if (k == 1 and (array[2] == Z)):
                            count +=1
                        else :
                            flag = False
                    else:
                        flag = False

                tempXIndex = X
                tempYIndex = Y

            if (count >= 5) :
                max = 1
                break
            else:
                max = 0
        if max == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    game = Game()
    # game.init_fiveGroups()
    game1 = Game()

    print(game is game1)
