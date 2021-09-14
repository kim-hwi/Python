
def dfs(g, s, depth,dir):
    
    if s>=Y or s<0 or g>=X or g<0 or depth == L:
        return
    if arr[s][g] == 0 or vis[s][g] == 1:
        return
    if dir == 1:
        if arr[s][g] == 3 or arr[s][g] == 4 or arr[s][g] == 7:
            return
    if dir == 2:
        if arr[s][g] == 2 or arr[s][g] == 4 or arr[s][g] == 5:
            return
    if dir == 3:
        if arr[s][g] == 3 or arr[s][g] == 5 or arr[s][g] == 6:
            return
    if dir == 4:
        if arr[s][g] == 2 or arr[s][g] == 6 or arr[s][g] == 7:
            return
    if depth == 5:
        print(g, s, depth, dir)

    vis[s][g] = 1
    
    if arr[s][g] == 1:
        dfs(g+1, s,depth+1,2)
        dfs(g, s+1, depth+1,3)
        dfs(g-1, s, depth+1,4)
        dfs(g, s-1, depth+1,1)
    
    if arr[s][g] == 2:
        dfs(g, s+1, depth+1,3)
        dfs(g, s-1, depth+1,1)
    
    if arr[s][g] == 3:
        dfs(g+1, s, depth+1,2)
        dfs(g-1, s, depth+1,4)
    
    if arr[s][g] == 4:
        dfs(g+1, s, depth+1,2)
        dfs(g, s+1, depth+1,3)
    
    if arr[s][g] == 5:
        dfs(g+1, s, depth+1,2)
        dfs(g, s-1, depth+1,1)
    
    if arr[s][g] == 4:
        dfs(g-1, s, depth+1,4)
        dfs(g, s-1, depth+1,1)

    if arr[s][g] == 4:
        dfs(g-1, s, depth+1,4)
        dfs(g, s+1, depth+1,3)

T = int(input())


for test in range(1, T + 1):
    
    Y,X,y,x,L=map(int,input().split(' '))
    arr = [[int(i) for i in input().split(' ')] for j in range(Y)]
    vis = [[0 for i in range(X)] for j in range(Y)]
    dfs(x,y,0,0)
    
    ans=0
    for i in vis:
        for j in i:
            if j==1:
                ans+=1

    print('#',test,' ',ans,sep='')