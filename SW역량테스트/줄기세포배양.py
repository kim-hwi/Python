T = int(input())
from collections import deque
dix = [-1,0,1,0]
diy = [0,1,0,-1]
for t in range(T):
    board = [[0 for i in range(1000)]for j in range(1000)]
    vis = [[0 for i in range(1000)]for j in range(1000)]
    M, N, K = map(int, input().split())
    
    qu=deque()
    for x in range(N):
        y=0
        for i in input().split():
            i = int(i)
            board[500+x][500+y] = i
            vis[500+x][500+y] = 1
            if i != 0:
                qu.append([500+x, 500+y, i, i])
            y+=1
    k=0
    while k !=K:
        k+=1
        temp = deque()
        while len(qu) != 0:
            cur = qu.popleft()
            
            if cur[3] == 0:
                board[cur[0]][cur[1]] =-1
                vis[cur[0]][cur[1]] = 1
                for dir in range(4):
                    nx = cur[0]+dix[dir]
                    ny = cur[1]+diy[dir]
                    if board[nx][ny] == -1:
                        continue

                    elif board[nx][ny] == 0:
                        board[nx][ny] = cur[2]
                        temp.append([nx, ny, cur[2], cur[2]])

                    elif board[nx][ny] < cur[2] and vis[nx][ny] == 0:
                        board[nx][ny] = cur[2]
                        temp.append([nx, ny, cur[2], cur[2]])

                    
                   

            else:
                temp.append([cur[0],cur[1],cur[2],cur[3]-1])
        ta = len(temp)
        while len(temp) != 0:
            
            cur2 = temp.popleft()
            if board[cur2[0]][cur2[1]] == cur2[2]:
                vis[cur2[0]][cur2[1]] = 1
                qu.append(cur2)
        print(len(qu),ta)
        cou=0
    for i in range(490,515):
        c=0
        for l in range(1,11):
            c+=board[i].count(l)
        cou+=c
        print(board[i][490:515])
    print(cou,len(qu))


            



            
    
    print(qu)
