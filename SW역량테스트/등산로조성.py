from collections import deque
t= int(input())
ans =[]
dix = [1,0,-1,0]
diy = [0,1,0,-1]
N=0


def dfs(curx, cury, dist, flag, lenth,boardtemp):
    
    for dir in range(4):
        board = boardtemp.copy()
        ndist = dist.copy()
        nx = curx+dix[dir]
        ny = cury+diy[dir]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if board[nx][ny] < board[curx][cury] and ndist[nx][ny] == 0:
            ndist[nx][ny] = ndist[curx][cury]+1
            dfs(nx, ny, ndist, flag, lenth+1,board)
            ndist[nx][ny] = 0
        elif board[nx][ny] >= board[curx][cury] and ndist[nx][ny] == 0:
            if flag != 1 and board[nx][ny] - board[curx][cury] < k and ndist[nx][ny] == 0:
                ndist[nx][ny] = ndist[curx][cury]+1
                temp = board[nx][ny]
                board[nx][ny] = board[curx][cury]-1

                dfs(nx, ny, ndist, 1, lenth+1,board)
                ndist[nx][ny] = 0
                board[nx][ny]=temp
                # print('el')
    ans.append(lenth)
    # for i in ndist:
    #     print(i)
    # print()
    # for i in ndist:
    #     print(i)
    # print()



for t in range(t):
    ans.clear()
    n,k=map(int,input().split())
    board1 = [[int(i) for i in input().split(' ')]for j in range(n)]
    dist1 = [[0 for i in range(n)]for j in range(n)]
    start=deque()
    maxnum=0
    for i in range(n):
        maxnum=max(maxnum,max(board1[i]))
    for i in range(n):
        for j in range(n):
            if board1[i][j] == maxnum:
                start.append([i,j])
    for i in start:
        dist1[i[0]][i[1]]= 1
        dfs(i[0],i[1],dist1,0,1,board1)
        dist1[i[0]][i[1]] = 0
        # print('~~~~~~~~~~~~~~~~~~~`')
    print('#',t+1,' ',max(ans),sep='')
    
