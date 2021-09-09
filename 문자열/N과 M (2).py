import itertools

N,M = map(int,input().split())

arr = [i for i in range(1,N+1)]
arr = sorted(list(itertools.combinations(arr,M)))
for i in range(len(arr)):
    for j in range(M):
        print(arr[i][j],end=' ')
    print()
# print(arr)
