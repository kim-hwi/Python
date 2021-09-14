from collections import deque
m,n = map(int,input().split(' '))
board = [[i for i in map(int,input().split(' '))]for j in range(n)]
dist =[[-1 for i in range(m)]for j in range(n)]
# print(board)
dix=[1,0,-1,0]
diy=[0,1,0,-1]
qu=deque([])

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            qu.append([i,j])
            dist[i][j] = 0
if len(qu) == n*m:
    print(0)
    exit(0)

while(len(qu)!=0):
    cur = qu.popleft()
    for i in range(4):
        nx = dix[i]+cur[0]
        ny = diy[i]+cur[1]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if board[nx][ny] == 1 or board[nx][ny] == -1 or dist[nx][ny] != -1:
            continue
        board[nx][ny] = 1
        dist[nx][ny] = dist[cur[0]][cur[1]]+1
        qu.append([nx,ny])
ans = 0
# print(dist)
for i in range(n):
    for j in range(m):
        ans=max(ans,dist[i][j])
        if dist[i][j] == -1 and board[i][j] == 0:
            print(-1)
            exit(0)
print(ans)




