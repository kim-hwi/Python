testcase = int(input())
arr = [0 for i in range(testcase)]
for i in range(testcase):
    arr[i] = int(input())
arr.sort()
for i in arr:
    print(i)
