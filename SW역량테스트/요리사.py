def syn(arr):
    res = 0
    for i in arr:
        for j in arr:
            if i != j:
               res+=food[i][j] 
    return  res

def dfs (idx,k):
    global res
    if idx == N//2:
        A=[]
        B=[]
        for i in range(len(vis)):
            if vis[i] == 1:
                A.append(i)
            else:
                B.append(i)
        # print(A,B)
        score1 = syn(A)
        score2 = syn(B)
        
        res = min(abs(score1-score2),res)
        return
    for i in range(k,N):
        if vis[i] != 1:
            vis[i] = 1
            dfs(idx+1,i+1)
            vis[i] = 0

T=int(input())

for test_case in range(1, T + 1):
    N=int(input())
    food=[list(map(int, input().split(' '))) for _ in range(N)]
    vis=[0 for i in range(N)]
    res=9999999
    dfs(0, 0)
    print('#',test_case,' ',res,sep='')
    
    



