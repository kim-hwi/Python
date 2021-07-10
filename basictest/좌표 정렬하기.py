testcase = int(input())
arr = [[0,0] for i in range(testcase)]
for i in range(testcase):
    arr[i][0],arr[i][1] = map(int,input().split())
arr.sort()
for i in range(testcase):
    print(arr[i][0],arr[i][1])
