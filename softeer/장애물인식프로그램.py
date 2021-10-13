import sys
from collections import deque
dix = [-1, 0, 1, 0]
diy = [0, 1, 0, -1]


count = []
blu = 0
n = int(input())
arr = [[int(i) for i in input()]for j in range(n)]
vis = [[False for i in range(n)]for j in range(n)]
# for i in range(n):
#     print(arr[i])
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and vis[i][j] == False:
            cou = 1
            blu += 1
            qu = deque()
            qu.append([i, j])
            vis[i][j] = True
            while qu:
                curx, cury = qu.popleft()
                for dir in range(4):
                    nx = curx+dix[dir]
                    ny = cury+diy[dir]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if arr[nx][ny] == 0 or vis[nx][ny] == True:
                        continue
                    qu.append([nx, ny])
                    vis[nx][ny] = True
                    cou += 1
            count.append(cou)
print(blu)
count.sort()
for i in count:
    print(i)
