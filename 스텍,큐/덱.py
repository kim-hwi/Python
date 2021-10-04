import sys
from collections import deque

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
# ?
num = int(input())
qu=deque()
for i in range(num):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'push_front':
        qu.appendleft(cmd[1])
    
    if cmd[0] == 'push_back':
        qu.append(cmd[1])
    
    if cmd[0] == 'pop_front':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu.popleft())
    
    if cmd[0] == 'pop_back':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu.pop())
    
    if cmd[0] == 'size':
        print(len(qu))
    
    if cmd[0] == 'empty':
        if len(qu) == 0:
            print(1)
        else:
            print(0)
    
    if cmd[0] == 'front':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[0])

    if cmd[0] == 'back':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[-1])
        
