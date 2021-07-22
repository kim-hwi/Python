N,M = map(int,input().split())
visted = [False for i in range(N+1)]
buffer = []
def dfs (depth,N,M):
    if M+1 == depth:
        for i in range(M):
            print(buffer[i],end=" ")
        print()
        return
    for i in range(1,N+1):
        if not visted[i]:
            visted[i]=True
            buffer.append(i)
            dfs(depth+1,N,M)
            visted[i]=False
            buffer.pop()
dfs(1,N,M)





























# N, M = map(int, input().split())  # M = depth
# result = []
# visitied = [False]*(N+1)
# # print(visitied)

# def dfs(depth, N, M):
#     if depth == M+1:  # 깊이까지 탐색 완료
#         for i in range(0, len(result)):
#             print(result[i], end=" ")
#         print()
#         return
#     for num in range(1, N+1):
#         if not visitied[num]:
#             visitied[num] = True
#             result.append(num)
#             dfs(depth+1, N, M)
#             visitied[num] = False
#             result.pop()
# dfs(1, N, M)
