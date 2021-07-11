num = int(input())
arr = [[0,0,'']for i in range(num)]
for i in range(num):
    arr[i][0] = i
    arr[i][1],arr[i][2] = map(str,input().split())
arr.sort(key = lambda x:(int(x[1]),int(x[0])))
for i in range(num):
    print(arr[i][1],arr[i][2])
