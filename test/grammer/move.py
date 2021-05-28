# S = [(1,'eps',2),(2,'a',3),(3,'eps',6),(1,'eps',4),(5,'eps',6),(6,'eps',1)]
S = [(0,'eps',1),(0,'eps',7),(1,'eps',2),(1,'eps',4),(2,'a',3),
     (3,'eps',6),(4,'b',5),(5,'eps',6),(6,'eps',1),(6,'eps',7),(7,'a',8),
     (8,'b',9),(9,'b',10)]
result = []
def p_closure(p):
    T=[]
    T1=[p]

    while len(T) != len(T1):
        T=[q for q in T1]

        for q in T:
            for t0,sym,t1 in S:
                if t0 == q and sym == 'eps' and t1 not in T1:
                    T1.append(t1)
    T1.sort()
    return T1

def p_move(I,a):
    T1=[]
    for q in I:
        for t0, sym, t1 in S:
            if t0 == q and sym == a and t1 not in T1:
                T1.append(t1)
    T1.sort()
    return T1

def p_closure_move(I):
    T1=[]
    for p in I:
        for i in p_closure(p):
            if i not in T1:
                T1.append(i)
    T1.sort()
    return T1



print(p_closure(0))
T0=p_closure(0)

print(p_closure_move(p_move(T0,'b')))
