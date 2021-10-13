# N,M = map(int,input().split())
# board = []
# dirX = [1,0,-1,0]
# dirY = [0,1,0,-1]
# vis = [[False for i in range(M)]for j in range(N)]
# dist = [[-1 for i in range(M)]for j in range(N)]

# for i in range(N):
#     board.append(str(input()))



# arr = [[0,0]]
# dist[0][0] = 0
# while len(arr) != 0:
#     cur = arr.pop(0)
#     for dir in range(4):
#         nx = cur[0]+dirX[dir]
#         ny = cur[1]+dirY[dir]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#         if dist[nx][ny] >= 0 or board[nx][ny] != '1':
#             continue
#         dist[nx][ny] = dist[cur[0]][cur[1]]+1
#         arr.append([nx,ny])

# print(dist[N-1][M-1]+1); 



dix = [1,0,-1,0]
diy = [0,1,0,-1]

n,m = map(int,input().split())

arr = [[int(i) for i in input()]for j in range(n)]
dist = [[10001 for i in range(m)]for j in range(m)]
dist[0][0] = 0
qu=[[0,0]]

while qu:
    cur = qu.pop(0)
    
    for dir in range(4):
        nx = cur[0]+dix[dir]
        ny = cur[1]+diy[dir]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if dist[cur[0]][cur[1]]+1<dist[nx][ny] and arr[nx][ny] == 1:
            dist[nx][ny] = dist[cur[0]][cur[1]]+1
            qu.append([nx,ny])



# print(arr)
# for i in range(n):
#     print(dist[i])
print(dist[n-1][m-1]+1)
