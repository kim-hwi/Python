testcase = int(input())
big = [0,0]
arr = [[0 for i in range(3)] for j in range(testcase)]
for i in range(testcase):
    arr[i][2] = 0
for i in range(testcase):
    arr[i][0],arr[i][1] = map(int,input().split())
for i in range(testcase):
    count = 1
    for j in range(testcase):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1] and arr[i][2] == 0:
            count+=1
    arr[i][2] = count
for i in range(testcase):
    print(arr[i][2],end=' ')
