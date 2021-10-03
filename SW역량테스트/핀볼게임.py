from typing import Tuple


T = int(input())

dix=[-1,0,1,0]
diy=[0,1,0,-1]

for t in range(T):
    N = int(input())
    board = [[int(i) for i in input().split()]for j in range(N)]
    score=[]
    for i in range(N):
        for j in range(N):
            start=[i,j]
            if board[i][j] != 0:
                continue
            for dir in range(4):
                soc=0
                nx = i+dix[dir]
                ny = j+diy[dir]
                while True:
                    if nx == start[0] and ny == start[1]:
                        score.append(soc)
                        break
                    

                    
                    if board[nx][ny] == 1:
                        if dir == 0:
                            dir = 2
                        if dir == 1:
                            dir = 3
                        if dir == 2:
                            dir = 1
                        if dir == 3:
                            dir = 0
                        soc += 1
                    if board[nx][ny] == 2:
                        if dir == 0:
                            dir = 1
                        if dir == 1:
                            dir = 3
                        if dir == 2:
                            dir = 0
                        if dir == 3:
                            dir = 2
                        soc += 1
                    if board[nx][ny] == 3:
                        if dir == 0:
                            dir = 3
                        if dir == 1:
                            dir = 2
                        if dir == 2:
                            dir = 0
                        if dir == 3:
                            dir = 1
                        soc += 1
                    if board[nx][ny] == 4:
                        if dir == 0:
                            dir = 2
                        if dir == 1:
                            dir = 0
                        if dir == 2:
                            dir = 3
                        if dir == 3:
                            dir = 1
                        soc += 1
                    if board[nx][ny] == 5:
                        if dir == 0:
                            dir = 2
                        if dir == 1:
                            dir = 3
                        if dir == 2:
                            dir = 0
                        if dir == 3:
                            dir = 1
                        soc += 1

                    # if nx < N and nx >= 0 and ny < N and ny >= 0:
                    #     if board[nx][ny] > 5 and board[nx][ny] < 11:
                    #         flag = False
                    #         for l in range(N):
                    #             if flag == True:
                    #                 break
                    #             for k in range(N):
                    #                 if board[l][k] == board[nx][ny]:
                    #                     nx = l
                    #                     ny = k
                    #                     flag = True
                    #                     break

                    if nx < N and nx >= 0 and ny < N and ny >= 0:
                        if board[nx][ny] == -1:
                            score.append(soc)
                            break

                    if nx < 0:
                        dir = 2
                        soc += 1
                    if nx >= N:
                        dir = 0
                        soc += 1
                    if ny < 0:
                        dir = 1
                        soc += 1
                    if ny >= N:
                        dir = 3
                        soc += 1

                    nx = nx+dix[dir]
                    ny = ny+diy[dir]
                    print(board[nx][ny],dir,nx,ny,start)
                    print()   
                    
                    

    print(score)
