List = [[1,3],[2,3],[2,2],[3,2],[1,3],[2,3],[2,2],[3,3]]
child = {}
for i in List:
    if i[0] in child:
      if child[i[0]] < i[1]:
          child[i[0]] = i[1]
    else:
        child[i[0]] = i[1]

    if i[0]+1 not in child:
        child[i[0]+1] = 0
dic = {
    1:3,
    2:3,
    3:2
}
print(child,len(child))