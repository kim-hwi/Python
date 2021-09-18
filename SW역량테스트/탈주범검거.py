from collections import deque
T = int(input())

dix = [0,-1,0,1]
diy = [1,0,-1,0]


for test in range(1, T + 1):
    
    X,Y,x,y,L=map(int,input().split(' '))
    board = [[int(i) for i in input().split(' ')] for j in range(X)]
    dist = [[0 for i in range(Y)] for j in range(X)]
    dist[x][y] = 1
    qu = deque()
    qu.append([x,y])
    while len(qu) != 0:
        cur = qu.popleft()
        # print(cur)
        for i in range(4):
            if i == 0 and (board[cur[0]][cur[1]] == 1 or board[cur[0]][cur[1]] == 3 or board[cur[0]][cur[1]] == 4 or board[cur[0]][cur[1]] == 5):
                nx = cur[0]+dix[i]
                ny = cur[1]+diy[i]
                
                if nx<0 or ny<0 or nx>=X or ny>=Y:
                    continue
                # print(board[nx][ny],nx,ny)
                if dist[nx][ny] == 0 and (board[nx][ny] == 1 or board[nx][ny] == 3 or board[nx][ny] == 6 or board[nx][ny] == 7):
                    qu.append([nx,ny])
                    dist[nx][ny] = dist[cur[0]][cur[1]]+1
                    
            if i == 1 and (board[cur[0]][cur[1]] == 1 or board[cur[0]][cur[1]] == 2 or board[cur[0]][cur[1]] == 4 or board[cur[0]][cur[1]] == 7):
                nx = cur[0]+dix[i]
                ny = cur[1]+diy[i]
                if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                    continue
                if dist[nx][ny] == 0 and (board[nx][ny] == 1 or board[nx][ny] == 2 or board[nx][ny] == 5 or board[nx][ny] == 6):
                    qu.append([nx, ny])
                    dist[nx][ny] = dist[cur[0]][cur[1]]+1
            if i == 2 and (board[cur[0]][cur[1]] == 1 or board[cur[0]][cur[1]] == 3 or board[cur[0]][cur[1]] == 6 or board[cur[0]][cur[1]] == 7):
                nx = cur[0]+dix[i]
                ny = cur[1]+diy[i]
                if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                    continue
                if dist[nx][ny] == 0 and (board[nx][ny] == 1 or board[nx][ny] == 3 or board[nx][ny] == 4 or board[nx][ny] == 5):
                    qu.append([nx, ny])
                    dist[nx][ny] = dist[cur[0]][cur[1]]+1
            if i == 3 and (board[cur[0]][cur[1]] == 1 or board[cur[0]][cur[1]] == 2 or board[cur[0]][cur[1]] == 5 or board[cur[0]][cur[1]] == 6):
                nx = cur[0]+dix[i]
                ny = cur[1]+diy[i]
                if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                    continue
                
                if dist[nx][ny] == 0 and (board[nx][ny] == 1 or board[nx][ny] == 2 or board[nx][ny] == 4 or board[nx][ny] == 7):
                    qu.append([nx, ny])
                    dist[nx][ny] = dist[cur[0]][cur[1]]+1
   
    count = 0
    for i in range(X):
        for j in range(Y):
            if dist[i][j] <= L and dist[i][j] != 0:
                count+=1
    print('#',test,' ',count,sep='')
