import copy
from collections import deque

dix = [0,1,0,-1]
diy = [-1,0,1,0]

def dfs (boardtemp,n):
    global W
    global H
    global ans
    if n == 0:
        num = 0
        for i in range(W):
            num += H - boardtemp[i].count(0)
        ans.append(num)
        return
    for loc in range(W):
        boards=copy.deepcopy(boardtemp) #2차원 배열이기 때문에 deepcopy사용
        boom=deque() 
        for Y in range(H):
            if boards[loc][Y] > 0:
                boom.append([loc,Y,boards[loc][Y]])
                while(len(boom)!=0):
                    cur = boom.popleft()
                    
                    for lenth in range(cur[2]-1):
                        for dir in range(4):
                            nx = cur[0]+dix[dir]*(lenth+1)
                            ny = cur[1]+diy[dir]*(lenth+1) #상좌하우 순으로 + 하나씩 더 넓어지는 과정
                            
                            if nx >= W or nx<0 or ny >= H or ny<0:
                                continue
                            
                            if boards[nx][ny]>0:
                                boom.append([nx,ny,boards[nx][ny]])
                    boards[cur[0]][cur[1]] = 0

                break # 첫번째 열에서 벽돌을 만나면 다음 돌을 처리하지않음
        for i in range(W):
                    for j in range(1,H):
                        if boards[i][j]==0:
                            boards[i].pop(j)
                            boards[i].insert(0,0)
        

        dfs(boards, n-1) # 다음단계 실행

T = int(input())
for t in range(T):
    N,W,H = map(int,input().split())
    ans=[]
    board=[[] for i in range(W)]
    for j in range(H):
        num = 0
        for i in input().split():
            board[num].append(int(i))
            num+=1
    dfs(board, N)
    print('#',t+1,' ',min(ans),sep='')
