ans=[]

def dfs (depth,n,t):
    global ans
    global vis
    global num
    # print(depth,n,t)
    if depth == t:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        if len(ans)>0:
            if ans[-1] < num[i]:
                vis[i] = True
                ans.append(num[i])
                dfs(depth+1,n,t)
                vis[i] = False
                ans.pop()
        else:
            vis[i] = True
            ans.append(num[i])
            dfs(depth+1, n, t)
            vis[i] = False
            ans.pop()


while True:
    
    num = list(map(int,input().split()))
    if num[0] == 0:
        exit(0)
    N = num[0]
    num=num[1:]
    
    vis = [False for i in range(N)]
    
    
    
    num.sort()
    dfs(0,N,6)
    print()
   
    
