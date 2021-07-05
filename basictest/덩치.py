testcase = int(input())
count = 1
big = [0,0]
arr = [[0 for i in range(3)] for j in range(testcase)]
for i in testcase:
    arr[3] = 0
for i in range(testcase):
    arr[i][0],arr[i][1] = map(int,input().split())
for i in range(testcase):
    for j in range(testcase):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][0] and arr[i][3] != 0:
            big = [arr[i][0],arr[i][1]]
            

print(",,",arr[1][0],arr[1][1])
