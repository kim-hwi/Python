import sys
from collections import deque

cmd = int(input())
qu = deque()
for c in range(cmd):
    push = list(map(str, sys.stdin.readline().split()))
    # print(push[0])
    if push[0] == 'push':
        qu.append(push[1])
        # print(push[1])
    
    if push[0] == 'pop':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu.popleft())
    
    if push[0] == 'size':
        print(len(qu))
    
    if push[0] == 'empty':
        if len(qu) == 0:
            print(1)
        else:
            print(0)
    
    if push[0] == 'front':
        if len(qu) == 0:
            print(-1)
        else:
            temp = qu.popleft()
            print(temp)
            qu.appendleft(temp)

    if push[0] == 'back':
        if len(qu) == 0:
            print(-1)
        else:
            temp = qu.pop()
            print(temp)
            qu.append(temp)
     
