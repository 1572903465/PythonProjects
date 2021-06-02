# List = [[1,3],[2,3],[2,2],[3,2],[1,3],[2,3],[2,2],[3,3]]
# child = {}
# for i in List:
#     if i[0] in child:
#       if child[i[0]] < i[1]:
#           child[i[0]] = i[1]
#     else:
#         child[i[0]] = i[1]
#
#     if i[0]+1 not in child:
#         child[i[0]+1] = 0
# dic = {
#     1:3,
#     2:3,
#     3:2
# }
# print(child,len(child))
inder_list = [1,2,3,4,5,6,7,8,9]
colums_list = [1,2,3,4,5,6,7,8,9]
count = 0
count2 = 0
for i in inder_list:
    count = count2
    count2 += 1
    list = []
    for j in colums_list:
        if count < 0:
            list.append(i-j)
        count-=1

    print(list)