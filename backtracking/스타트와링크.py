n =int(input())
board = [[int(i) for i in input().split()]for j in range(n)]
# vis =[[False for i in range(n)]for j in range(n)]
vis = [False for i in range(n)]
ans = 999999999


def cal(bod):
    # print(board)
    tot=0
    for i in bod:
        for j in bod:
            
            if j == i:
                continue
            # print(board[i][j],i,j)
            tot+=board[i][j]
    return tot

def dfs (k):
    global ans
    if vis.count(True) == int(n/2):
        
        s = []
        l = []
        
        for i in range(len(vis)):
            if(vis[i]) == True:
                s.append(i)
            else:
                l.append(i)
       
        ans=min(abs(cal(s)-cal(l)),ans)
        return
    for i in range(k,n):
        if vis[i]==False:
            vis[i]=True
            dfs(i+1)
            vis[i]=False
dfs(0)
print(ans)

