N,M = map(int,input().split())
vist = [[False]*(N+1)]*(N+1)
buffer = []
print(vist)

def dfs(depth,N,M):
    if M+1 == depth:
        print(depth)
        for i in range(M):
            print(buffer[i],end=" ")
        print()
        return
    for i in range(1,N+1):
        for j in range(1,N+1):
            if vist[i][j]==False:
                buffer.append(i)
                print(depth)
        vist[i][j]=True
        dfs(depth+1,N,M)
        buffer.pop()
dfs(1,N,M)
