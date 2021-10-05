E,S,M = list(map(int,input().split()))
e=0
s=0
m=0
t=0
while True:
    if e==E and s ==S and M ==m:
        print(t)
        break
    e+=1
    s+=1
    m+=1
    if e>15:
        e=1
    if s>28:
        s=1
    if m>19:
        m=1
    t+=1