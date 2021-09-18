N,M = map(int,input().split())
board = []
dirX = [1,0,-1,0]
dirY = [0,1,0,-1]
vis = [[False for i in range(M)]for j in range(N)]
dist = [[-1 for i in range(M)]for j in range(N)]

for i in range(N):
    board.append(str(input()))



arr = [[0,0]]
dist[0][0] = 0
while len(arr) != 0:
    cur = arr.pop(0)
    for dir in range(4):
        nx = cur[0]+dirX[dir]
        ny = cur[1]+dirY[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if dist[nx][ny] >= 0 or board[nx][ny] != '1':
            continue
        dist[nx][ny] = dist[cur[0]][cur[1]]+1
        arr.append([nx,ny])

print(dist[N-1][M-1]+1); 
