def fiveGroups():
    fiveGroup = []
    # 纵向的
    for y in range(1,16):
        for x in range(1,12):
            fiveGroup.append([[x,y],[x+1,y],[x+2,y],[x+3,y],[x+4,y]])
    # print(1,len(fiveGroup))
    # 横向的
    for x in range(1,16):
        for y in range(1,12):
            fiveGroup.append([[x,y],[x,y+1],[x,y+2],[x,y+3],[x,y+4]])
    # print(2,len(fiveGroup))
    #  '/'左半边
    for y in range(5,16):
        for l in range(1,y-4):
            fiveGroup.append([[l,y],[l+1,y-1],[l+2,y-2],[l+3,y-3],[l+4,y-4]])
    # print(3,len(fiveGroup))
    #  '/'右半边
    for x in range(2,12):
        for l in range(15,x+2,-1):
            fiveGroup.append([[x, l], [x+1, l - 1], [x+1, l - 2], [x+1, l -3], [x+1, l - 4]])
    # '\'左部分
    # print(4,len(fiveGroup))
    for x in range(11, 0,-1):
        for l in range(1, 12-x):
            fiveGroup.append([[x, l], [x + 1, l + 1], [x + 1, l + 2], [x + 1, l + 3], [x + 1, l + 4]])
    # '\' 右部分
    # print(5,len(fiveGroup))
    for y in range(2, 12):
        for l in range(1, 13-y):
            fiveGroup.append([[y, l], [y + 1, l + 1], [y + 2, l + 2], [y + 3, l + 3], [y + 4, l + 4]])
    print(6,len(fiveGroup))
    # print(fiveGroup)

if __name__ == '__main__':
    fiveGroups()
