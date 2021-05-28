import operator

class Stack(object):
    def __init__(self):
        self.__data = []

    def is_empty(self):
        """判断栈是否为空"""
        return self.__data == []

    def push(self, data):
        """在栈顶添加元素"""
        self.__data.append(data)

    def pop(self):
        """弹出顶部元素"""
        return self.__data.pop()

    def peek(self):
        """返回栈顶元素"""
        # 先判断是否为空
        if self.is_empty():
            return
        else:
            return self.__data[-1]

    def size(self):
        """判断长度"""
        return len(self.__data)

    def travel(self):
        """遍历所有元素"""
        self.__data = self.__data[::-1]
        for i in self.__data:
            print(i)

VT = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'
    , 'U', 'V', 'W', 'X', 'Y', 'Z']


def input_Grammer():  # 输入文法
    with open('input.txt', 'r', encoding='utf-8') as f:
        G = [line.strip('\n') for line in f.readlines()]
    # print(G)
    D = []
    for i in G:
        D.append(i.split('->'))
    print(D)
    # D1={}
    # for i in D:
    #     # print(i)
    #     D3 = [k for k in i]
    #     del D3[0]
    #     D1[i[0]] = D3
    # print(D1)
    return D


def FIRST_P(D):  # 计算FISRT集合

    # print(D)
    T = []
    T1 = []
    left = []  # 记录已经拥有FRIST集合的左部集合，注意不能使用for时候的当前项i的左部，因为只是一个左部而不是全部的左部
    for i in D:
        if i[0] not in left:
            T.append([i[0]])
            left.append(i[0])
    # for i in T:
    #     print(i)
    while not operator.eq(T, T1):
        T1.clear()
        for i in T:
            d = [q for q in i]
            T1.append(d)
        for i in D:  # i[0]是左部
            if i[0] not in VT and i[0] != '0':  # X属于终结符
                for j in T:
                    if i[1][0] not in j and i[0] == j[0]:  # 左部存在，终结符第一次出并且不存在列表里面
                        j.append(i[1][0])

            if i[0] in VT and i[1][0] not in VT:  # X属于非终结符并且X->a... a属于终结符 右部含有终极符开头的串
                for j in T:
                    if i[1][0] not in j and i[0] == j[0]:  # 左部存在，终结符第一次出现不存在列表里面
                        j.append(i[1][0])

            if i[0] in VT and i[1][0] in VT:
                count = 0
                while True:
                    # print(T[left.index(i[1][count])])
                    if count < len(i[1]):
                        for j in T[left.index(i[1][count])]:
                            # print(T[left.index(i[1][count])])
                            if j not in T[left.index(i[0])] and j != '0' and j not in VT:
                                # print(j)
                                T[left.index(i[0])].append(j)
                            # print(count,len(i[1]))
                            if count == len(i[1]) - 1 and '0' in T[left.index(i[1][count])] and '0' not in T[left.index(i[0])]:
                                T[left.index(i[0])].append('0')
                        if '0' not in T[left.index(i[1][count])]:
                            break
                        count = count + 1
                    else:
                        break
    T2 = {}
    for i in T:
        # print(i)
        T3 = [k for k in i]
        del T3[0]
        T2[i[0]] = T3
    # print(T2)
    return T, T2


def FOLLOW_P(D, T, T2):# 计算FOLLOW集合
    # print(T)
    F = []
    F1 = []
    F2 = {}
    F3 = {}
    left = []  # 记录已经拥有FOLLOW集合的左部集合，注意不能使用for时候的当前项i的左部，因为只是一个左部而不是全部的左部
    for i in D:
        if i[0] not in left:
            F.append([i[0]])
            left.append(i[0])
            F2[i[0]] = []
    F[0].append('#')
    F2[left[0]].append('#')  # (1)  开始符号S集合的FOLLOW集合加入'#'
    # print(F2)
    while F2 != F3:
        for k in F2:
            # print(F2[k])
            temp = []
            # F3[k] = []
            for t in F2[k]:
                temp.append(t)
            F3[k] = temp
        # print(F3)
        for i in D:  # i[0]是左部
            count = 0
            while True:
                if count <= len(i[1]) - 2 and i[1][count] in VT and i[1][count + 1] not in VT and i[1][count + 1] not in \
                        F2[i[1][count]]:  # (2).1  X->...Ba  a是终极符
                    F[left.index(i[1][count])].append(i[1][count + 1])
                    F2[i[1][count]].append(i[1][count + 1])
                    # print(1, F2[i[1][count]])
                if count <= len(i[1])-2 and i[1][count] in VT and i[1][count + 1] in VT:  # (2).1  X->...BA  A是非终极符
                    temp = T2[i[1][count + 1]]
                    for t in temp:
                        if t not in F[left.index(i[1][count])] and t != '0':
                            F[left.index(i[1][count])].append(t)
                            F2[i[1][count]].append(t)
                    # print( F[left.index(i[1][count])])
                if count > len(i[1]) - 1:
                    break
                count = count + 1
            if i[0] in VT and i[1][len(i[1]) - 1] in VT:
                # print(i,i[0],i[1],i[1][len(i[1])-1],len(i[1]),F2[i[1][len(i[1])-1]],F2)
                count2 = 0
                while True:
                    if count2 < len(i[1]):
                        # print(F2[i[0]], F2[i[1][len(i[1]) - 1 - count2]])
                        for j in F2[i[0]]:
                            # print(i[1][len(i[1]) - 1 - count2])
                            if j != '0' and j not in F2[i[1][len(i[1]) - 1 - count2]]:
                                #（3）A->aBc  c能推出空  或  A->aB  FOllOW(A) 加入到FOLLOW（B）后面
                                F2[i[1][len(i[1]) - 1 - count2]].append(j)
                                # print(2, j, F2[i[1][len(i[1]) - 1 - count2]])
                        # # print(temp)
                        # break
                        if '0' not in T2[i[1][len(i[1]) - 1 - count2]] or i[1][len(i[1]) - 2 - count2] not in VT:
                            # print(i[1][len(i[1]) - 2 - count2])
                            break
                        count2 = count2 + 1
                    else:
                        break
    F.clear()
    # print(F)
    # print(F2)
    for i in F2:
        F.append([i]+F2[i])
    # print(F)
    return F,F2

def SELECT(D, T2, F2): #计算FOLLOW集合
    # print(D)
    # print(T2)
    R={}
    for i in D:
        R[i[-1]]=[]
    for i in D:
        if i[1][0] not in VT and i[1][0] !='0' and i[1][0] not in R[i[1]]:
            R[i[1]].append(i[1][0])
        if i[1][0] == '0' and '0' not in R[i[1]]:
            R[i[1]].append(i[1][0])
        if i[1][0] in VT:
            count = 0
            while True:
                if count < len(i[1]):
                    # print(T2[i[1][count]],count)
                    for j in T2[i[1][count]]:
                        if j not in R[i[1]] and j !='0':
                            R[i[1]].append(j)
                    if count == len(i[1]) - 1 and '0' in T2[i[1][count]] and 0 not in R[i[1]]:
                        R[i[1]].append('0')
                    if '0' not in T2[i[1][count]] or count == len(i[1]) - 1:
                        break
                    count = count + 1
                else:
                    break

            # print(i[1])
        # if len(i[1]) > 1 :
        #     if i[1][0] == '0' and i[1][1] not in VT:
        #         R[i[1]] = i[1][1]
        #     if i[1][0] == '0' and i[1][1] not in VT:
    S=[]   #SELECT 集D合
    for i in D:
        d = [q for q in i]
        S.append(d)
    # print(S)
    for i in S:
        if '0' not in R[i[1]]:
            temp = [v for v in R[i[1]]]
            i.append(temp)
            # print(i)
        if '0' in R[i[1]]:
            temp=[]
            for v in R[i[1]]:
                if v!='0' and v not in temp:
                    temp.append(v)
            for f in F2[i[0]]:
                if f != '0' and f not in temp:
                    temp.append(f)
            i.append(temp)
    # print(S)

    # for k in R:
    #     print('FISRT(%s)->'%k,R[k])
    return S,R
def predictive_annlysis_table(D,S): #构造文法的预测分析表
    # print(S)
    P=[]
    A = []
    PA = {}
    temp = []
    for i in D:
        for j in i[1]:
            if j not in VT and j !='0' and j not in  P:
                P.append(j)
        for j in i[0]:
            if j in VT and j != '0' and j not in P:
                PA[j] = []
    if '#' not in P:
        P.append('#')
    for i in P:
        temp.append(' ')
    for i in PA:
        te = [j for j in temp]
        PA[i]= te
    for i in S:
        temp1 = [i for i in PA[i[0]]]
        for j in i[2]:
            for k in P:
                if j == k and k not in VT:
                    temp1[P.index(k)] = i[1]
        PA[i[0]] = temp1
            # print(j)
    f ='\t\t'
    for i in P:
        f+=i+'\t\t'
    e = ''
    print('文化产生式的预测分析表为：')
    print(f)
    for i in PA:
        e += i +'\t\t'
        for j in PA[i]:
            e += j+'\t\t'

        print(e)
        e = ''
    return PA,P

    # print(PA)
# def re_string
def reverse(str):  # 字符串反置
    s =''
    for i in str:
        # print(str[len(str)-1-str.index(i)])
        s += str[len(str)-1-str.index(i)]
    return s


def analysi(PA,P):  # 输入串的分析过程
    s_stack = Stack()
    i_stack = Stack()
    a_stack = Stack()
    # str = input.txt("请输入符号串：\n")
    str = 'i+i*i#'
    analyse = '#E'
    for i in str:
        s_stack.push(i)
    # print(s_stack.travel())
    while not s_stack.is_empty():
        i_stack.push(s_stack.pop())
    # print(i_stack.size())
    # print(i_stack.travel())
    count= 1
    position = -1
    print('步骤','','分析栈','\t','剩余输出串')
    print(count, '\t', analyse, '\t', str)
    count += 1
    while len(str) >= 1 or len(analyse) >=1:
        match = str[0]
        key = analyse[len(analyse)-1]

        if match == '#' and len(analyse)==1 :
            # print(match,'####')
            if match == match :
                print('匹配成功')
                break
            else:
                print('匹配失败')
        position = P.index(match)
        if key in VT:
            temp = PA[key][position]
            if temp is None:
                print('匹配出错')

            if temp is '0':
                analyse = analyse[:-1]
                print(count,'\t',analyse, '\t', str)
                count += 1
            elif temp:
                analyse = analyse[:-1]
                analyse += reverse(temp)
                print(count, '\t', analyse, '\t', str)
                count += 1
        if key not in VT and key == match:

            str = str[1:]
            analyse = analyse[:-1]
            print(count, '\t', analyse, '\t', str)
            count += 1

        # print(position)


    # print(str[-1],len(str))

if __name__ == '__main__':
    # d = input.txt('请输入文法:\n')
    # while d != '#':
    #     d = input.txt('请输入文法:\n')
    #     g.append(d)
    D = input_Grammer()
    T, T2 = FIRST_P(D)
    F,F2=FOLLOW_P(D, T, T2)
    S,R= SELECT(D, T2, F2)
    # print(T2)
    print('文法左部的FIRST集合:')
    for k in T2:
        print('FIRST(%s)='%k,T2[k])
    # print(F2)
    print('文法左部的FOLLOW集合: ')
    for k in F2:
        print('FOLLOW(%s) =' % k, F2[k])
    print('文法产生式的SELECT集合:')
    for i in S:
        print('SELECT(%s->%s) ='% (i[0],i[1]) , i[2])

    PA,P = predictive_annlysis_table(D,S)

    analysi(PA,P)
