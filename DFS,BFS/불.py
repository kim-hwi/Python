from collections import deque
n,m=map(int,input().split(' '))
board = [list(input())for i in range(m)]

dix=[1,0,-1,0]
diy=[0,1,0,-1]

jqu = deque()
fqu = deque()

for i in range(len(board)):
    if 'F' in board[i]:
        fqu.append([i,board[i].index('F')])
    if 'J' in board[i]:
        jqu.append([i,board[i].index('J')])
        
count=1

while len(fqu) != 0 and len(jqu) != 0:
    # print(board)
    
    
    J = jqu.popleft()
    if J[0] >= n-1 or J[0] <= 0 or J[1] >= m-1 or J[1] <= 0:
        print(count)
        exit(0)
    count += 1
    for i in range(4):
        jnx = dix[i]+J[0]
        jny = diy[i]+J[1]
        
        if board[jnx][jny] == '#' or board[jnx][jny] == 'F' or board[jnx][jny] == 'J':    
            continue
        if jnx >= n-1 or jnx <= 0 or jny >= m-1 or jny <= 0:
            print(count)
            exit(0)
        board[jnx][jny] = 'J'
        jqu.append([jnx,jny])
    F = fqu.popleft()
    for i in range(4):
        fnx = dix[i]+F[0]
        fny = diy[i]+F[1]
        if fnx >= n or fnx < 0 or fny >= m or fny < 0:
            continue
        if board[fnx][fny] == '#' or board[fnx][fny] == 'F':
            continue
        board[fnx][fny] = 'F'
        fqu.append([fnx, fny])
    

print('IMPOSSIBLE')
