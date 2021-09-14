n,m = map(int,input().split(' '))
# board = [[input().split()] for j in range(n)]
arr = [input() for j in range(n)]
vis = [[0 for i in range(m)] for j in range(n)]

dix=[1,0,-1,0]
diy=[0,1,0,-1]

qu = []
qu.append([0,0])
vis[0][0] = 1
while(len(qu) != 0):
    
    temp = qu.pop(0)
    x = temp[0]
    y = temp[1]
    for dir in range(4):
        nx = dix[dir]+x
        ny = diy[dir]+y
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if arr[nx][ny] =='0' or (vis[nx][ny] != 0 and vis[nx][ny]-1 <= vis[x][y]):
            continue
        vis[nx][ny] = vis[x][y]+1
        qu.append([nx,ny])
        

print(vis[n-1][m-1])
