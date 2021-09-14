import itertools
N = str(input())
if '0' not in N:
    print(-1)
    exit(0)
num=0
arr=[]
for i in N:
    num+=int(i)
    arr.append(int(i))
if num%3 != 0:
    print(-1)
    exit(0)
arr.sort(reverse=True)
for i in arr:
    print(i,end='')