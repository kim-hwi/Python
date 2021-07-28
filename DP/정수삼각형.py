n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = list(map(int,input().split()))
res = [0]*n
for i in range(1,n):
    for j in range(len(arr[i])):
        if j==0:
            arr[i][j]+=arr[i-1][j]
            continue
        if j==len(arr[i])-1:
            arr[i][j]+=arr[i-1][j-1]
            continue
        arr[i][j]+=max(arr[i-1][j],arr[i-1][j-1])
print(max(max(arr)))
