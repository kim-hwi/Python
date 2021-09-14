n,m = input().split()
n=int(n)
m=int(m)
arr = [[i for i in input().split(' ')] for j in range(n)]
vis = [[0 for i in range(m)] for j in range(n)]
dirx=[1,0,-1,0]
diry=[0,1,0,-1]
maxarr=0
arrea=0
for i in range(n):
    for j in range(m):
        # print(i,j)
        if vis[i][j] == 1 or arr[i][j] =='0':
            continue
        vis[i][j] = 1
        qu = []
        qu.append([i,j])
        arrr = 0
        arrea+=1
        while(len(qu)!=0):
            arrr+=1
            temp = qu.pop(0)
            
            for l in range(4):
                
                nx = dirx[l]+temp[0]
                ny = diry[l]+temp[1]
                
                if nx<0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if vis[nx][ny] == 1 or arr[nx][ny] != '1':
                    continue
                # print(i, j, ny, nx, temp)
                vis[nx][ny] = 1
                qu.append([nx,ny])
        maxarr=max(arrr,maxarr)
        
print(arrea)
print(maxarr)
