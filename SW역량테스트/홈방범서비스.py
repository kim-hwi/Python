from collections import deque
T = int(input())

dix = [-1,0,1,0]
diy = [0,1,0,-1]

for t in range(T):
    N,M = map(int,input().split())
    board = [[int(i) for i in input().split()]for j in range(N)]
    vis = [[0 for i in range(N)]for j in range(N)]
    mony=0
    ans = 0
    for i in range(N):
        mony+=sum(board[i])
    mony*=M
    mset=1
    # print(mony)
    k=1
    # print(mony, mset, k)
    while mony>mset:
        k+=1
        mset = k*k+(k-1)*(k-1)
    k-=1
    mset = k*k+(k-1)*(k-1)

    for i in range(N):
        for j in range(N):
            count=0
            
            vis = [[0 for i in range(N)]for j in range(N)]
            qu = deque()
            qu.append([i,j,1])
            vis[i][j] = 1
            if board[i][j] != 0:
                count+=1
            if count*M >= 1*1:
                ans = max(ans, count)
            for K in range(k):
                while len(qu) != 0:
                    # print('???',qu[0])
                    if qu[0][2] != K:
                        break
                    cur = qu.popleft()
                    
                    for dir in range(4):
                        nx = cur[0]+dix[dir]
                        ny = cur[1]+diy[dir]
                        
                        if nx<0 or nx>=N or ny<0 or ny>=N:
                            continue
                        if vis[nx][ny] != 0:
                            continue
                        if board[nx][ny] != 0:
                            count+=1
                        
                        vis[nx][ny] = 1
                        qu.append([nx,ny,K+1])
                        # print(nx,ny,K)
                    
                    if count*M >= K*K+(K+1)*(K+1):
                        ans=max(ans,count)
                    # for u in range(N):
                    #     print(vis[u])
                    # print()


    # ans = max(ans, count)
    # print(mony,mset,k)
    print('#',t+1,' ',ans,sep='')
