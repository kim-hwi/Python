T = int(input())

for t in range(T):
    N,X=map(int,input().split())
    board = [[int(i) for i in input().split()]for j in range(N)]
    vis = [[0 for i in range(N)]for j in range(N)]
    # for i in range(N):
    #     print(board[i])
    count=[]
    for i in range(N):
        for j in range(N-1):
            if board[i][j]+1==board[i][j+1]:
                if j-X+1<0:
                    break
                flag = False
                for l in range(X):
                    if board[i][j]!=board[i][j-l] or vis[i][j-l] !=0:
                        flag = True
                if flag == True:
                    break
                for l in range(X):
                    vis[i][j-l] = 1
                    
            if board[i][j]-1 == board[i][j+1]:
                if j+X >= N:
                    break
                flag = False
                for l in range(X):
                    if board[i][j+1] != board[i][j+1+l] or vis[i][j+1+l] != 0:
                        flag = True
                if flag == True:
                    break
                for l in range(X):
                    vis[i][j+1+l] = 1
            
            if abs(board[i][j] - board[i][j+1]) > 1:
                break

            if j == N-2:
                count.append(i)
    vis = [[0 for i in range(N)]for j in range(N)]
    
    for j in range(N):
        for i in range(N-1):
            if board[i][j]+1 == board[i+1][j]:
                if i-X+1 < 0:
                    break
                flag = False
                for l in range(X):
                    if board[i][j] != board[i-l][j] or vis[i-l][j] != 0:
                        flag = True
                if flag == True:
                    break
                for l in range(X):
                    vis[i-l][j] = 1

            if board[i][j]-1 == board[i+1][j]:
                if i+X >= N:
                    break
                flag = False
                for l in range(X):
                    if board[i+1][j] != board[i+1+l][j] or vis[i+1+l][j] != 0:
                        flag = True
                if flag == True:
                    break
                for l in range(X):
                    vis[i+1+l][j] = 1

            if abs(board[i+1][j] - board[i][j]) > 1:
                break

            if i == N-2:
                count.append(j)
    
    
    # for i in range(N):
    #     print(vis[i])
    print('#',t+1,' ',len(count),sep='')


