n = int(input())
arr = [int(i) for i in input().split()]
vis = [1 for i in range(n)]
res = []


for i in range(0, n):
    m = 0
    for j in range(0, i):
        if arr[j] < arr[i]:
            m = max(m, vis[j])
    vis[i] = m+1
print(max(vis))
