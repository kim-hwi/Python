T = int(input())

dix=[-1,1,0,0]
diy=[0,0,-1,1]

for t in range(T):
    n,m,k=map(int,input().split(' '))
    board=[]
    vis=[[0 for i in range(n)]for j in range(n)]
    for i in range(k):
        board.append([int(i) for i in input().split(' ')])
    
    for time in range(m):
        vis = [[0 for i in range(n)]for j in range(n)]
        for boa in board:
            flag= True
            for dir in range(1,5):
                if dir==boa[3]:
                    nx = boa[0]+dix[dir-1]
                    ny = boa[1]+diy[dir-1]
                    # print(board[i],nx,ny)
            if nx>=n-1 or ny>=n-1 or nx<=0 or ny<=0:
                if boa[3] == 1:
                    boa[3]= 2
                elif boa[3] == 2:
                    boa[3] = 1
                elif boa[3] == 3:
                    boa[3] = 4
                elif boa[3] == 4:
                    boa[3] = 3
                boa[2] = int(boa[2]/2)
                if boa[2] == 0:
                    board.pop(board.index(boa))
                    flag = False
            if flag == False:
                continue
            boa[0]=nx
            boa[1]=ny
            vis[nx][ny]+=1
        
        for i in range(n):
            for j in range(n):
                if vis[i][j] >1:
                    temp=[]
                    for bo in board:
                        if bo[0]==i and bo[1]==j:
                            temp.append(board.index(bo))
                    num = -1
                    total=0
                    for l in temp:
                        total+=board[l][2]
                        num = max(board[l][2],num)
                    
                    for l in temp:
                        if board[l][2] == num:
                            board[l][2] = total
                            temp.pop(temp.index(l))
                    # print(temp)
                    while len(temp) != 0:
                        board.pop(temp.pop())
                    

        # print()
        # print()
        # for i in range(len(board)):
        #     print(board[i])
    
    # for i in range(len(board)):
    #         print(board[i])
    
    ans=0
    
    for i in board:
        ans+=i[2]
    print('#',t+1,' ',ans,sep='')


    
