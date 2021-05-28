# S = [(1,'eps',2),(2,'a',3),(3,'eps',6),(1,'eps',4),(5,'eps',6),(6,'eps',1)]
S = [(0, 'eps', 1), (0, 'eps', 7), (1, 'eps', 2), (1, 'eps', 4), (2, 'a', 3),
     (3, 'eps', 6), (4, 'b', 5), (5, 'eps', 6), (6, 'eps', 1), (6, 'eps', 7), (7, 'a', 8),
     (8, 'b', 9), (9, 'b', 10)]

# S=[(0,'a',1),(0,'b',1),(0,'b',2),(0,'a',3),(1,'b',1),(1,'a',3),(1,'b',2),(2,'b',4),(3,'a',4),(4,'a',4),(4,'b',4)]
# S=[(0,'a',0),(0,'b',0),(0,'eps',2),(2,'a',4),(2,'b',5),(4,'a',3),(5,'b',3),(3,'eps',0),(1,'a',1),(1,'b',1)]
def p_closure(p):  # 状态集的closure运算
    T = []
    T1 = [p]

    while len(T) != len(T1):
        T = [q for q in T1]

        for q in T:
            for t0, sym, t1 in S:
                if t0 == q and sym == 'eps' and t1 not in T1:
                    T1.append(t1)
    T1.sort()
    return T1


def p_move(I, a):# 状态集的move运算
    T1 = []
    for q in I:
        for t0, sym, t1 in S:
            if t0 == q and sym == a and t1 not in T1:
                T1.append(t1)

    T1.sort()
    return T1

def p_closure_move(I):
    T1 = []
    for p in I:
        for i in p_closure(p):
            if i not in T1:
                T1.append(i)
    T1.sort()
    return T1
def divideSubSet():  # NFA的子集化
    R=[] #NFA终态集合
    S=[0] #NFA初态集合
    SD=[]#DFA初态集合
    r = input('请输入终态的字符(按#结束输入）:\n')
    while r is not '#':
        R.append(int(r))
        r = input('请输入终态的字符:\n')
    print(R)
    F=[]  #DFA终态集合
    T=[]
    T1=[p_closure(0)]  #NFA子集
    print('子集化:',p_closure(0))
    Tup=[]  # DFA三元组
    # print(T)
    while len(T) != len(T1):
        T = [q for q in T1]
        for I in T:
            # print(T.index(I))
            A = p_move(I,'a')
            C = p_closure_move(A)
            if C not in T1 and C:
                print('子集化:',C)
                T1.append(C)
                # D.append(tup)
            if C:
                tup = (T1.index(I), 'a', T1.index(C))
                for d in C:
                    # print('c=', d)
                    if d in S and T1.index(C) not in F:
                        # print('ccc=', d)
                        F.append(T1.index(D))
                for i in I:
                    if i in S and T1.index(I) not in SD:
                        # print('ccc=', d)
                        SD.append(T1.index(I))

            if tup not in Tup:
                Tup.append(tup)
            B = p_move(I,'b')
            D = p_closure_move(B)
            if D not in T1 and D:
                print('子集化:',D)
                T1.append(D)
            if D:
                tup = (T1.index(I), 'b', T1.index(D))
                for d in D:
                    # print('d=',d)
                    if d in R and T1.index(D) not in F:
                        # print('d=', d)
                        F.append(T1.index(D))
                for i in I:
                    if i in S and T1.index(I) not in SD:
                        # print('ccc=', d)
                        SD.append(T1.index(I))
            if tup not in Tup:
                Tup.append(tup)
    return T1,Tup,F,SD

if __name__ == '__main__':
    Tup,D,F,SD= divideSubSet()
    print('NFA子集:',Tup)
    print('构造的DFAM:',D)
    print('DNA初态为：', SD)
    print('DNA终态为：',F)