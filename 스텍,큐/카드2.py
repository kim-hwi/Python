from collections import deque

num = int(input())
qu = deque()
for i in range(1,num+1):
    qu.append(i)
while len(qu) >1:
    # print(qu)
    qu.popleft()
    # print(qu)
    if len(qu) == 1:
        print(qu[0])
        exit(0)
    qu.append(qu.popleft())
print(qu[0],'/')


