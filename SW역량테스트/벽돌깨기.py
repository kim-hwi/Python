t= int(input())
ans=[]

def dfs (board2,N):
    global w
    res=0
    if N==0:
        # print(board2)
        for i in range(w):
            res+=sum(board2[i])
        ans.append(res)
        return
    tar=-1
    print(N)
    for i in range(w):
        board=board2.copy()
        # board = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 3, 1, 4, 4, 5, 6, 1, 7], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
        #     0, 0, 1, 2, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 2, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 2, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 2, 1, 1], [0, 0, 1, 9, 1, 1, 1, 1, 5, 1]]
        # if N == 3:
        
        for j in range(len(board2[i])):
            
            if board2[i][j] != 0 and j < len(board2[i]):    
                
                
                for k in range(len(board[i])):
                    if board[i][k]>0:
                        board[i][k]=board[i][k]-1
                    if board[i][k]<=0:
                        board[i].pop(k)
                        board[i].insert(0,0)
                for k in range(w):
                    if k==i:
                        continue
                    if board[k][j] > 0:
                        board[k][j] = board[k][j]-1
                    if board[k][j] <= 0:
                        board[k].pop(j)
                        board[k].insert(0, 0)
                print(i,j, N,board)
                print()
                board4=board.copy()
                dfs(board4, N-1)
                break
                

                
            
    


for tc in range(t):
    n,w,h = map(int,input().split())
    board3=[[] for i in range(w)]
    
    
    for j in range(h):
        num = 0
        for i in input().split(' '):
            board3[num].append(int(i))
            num+=1
    dfs(board3,n)
    # print(ans)

    

    
    # print(board)
