def volunteer(s, t, sn, tn):
    S = []
    curTime = s
    while curTime < t:
        nextVol, _ = max(enumerate(tn), key = lambda x : x[1] if sn[x[0]] <= curTime else 0)
        S.append(nextVol + 1)
        curTime = tn[nextVol]
    return sorted(S)

s1 = int(input())
t1 = int(input())
n = int(input())
sl = []
tl = []
for i in range(n):
    x,y = [int(x) for x in input().split()]
    sl.append(x)
    tl.append(y)
result = volunteer(s1, t1, sl, tl)
print(' '.join(map(str, result))) 
        
        
