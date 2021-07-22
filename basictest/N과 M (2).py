N,M = map(int,input().split())
vist = [False for i in range(N+1)]
buffer = []

def dfs(depth,N,M):
    if M+1 == depth:
        for i in range(M-1):
            if buffer[i]>buffer[i+1]:
                return
        for i in range(M):
            print(buffer[i],end=" ")
        print()
        return
    for i in range(1,N+1):
        if vist[i] == False:
            buffer.append(i)
            vist[i] = True
            dfs(depth+1,N,M)
            vist[i] = False
            buffer.pop()
dfs(1,N,M)
