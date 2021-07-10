testcase = int(input())
arr = [' ' for i in range(testcase)]
for i in range(testcase):
    temp = input()
    if temp in arr:
        continue
    else:
        arr[i] = temp
arr.sort(key=len)
for i in range(testcase):
    if arr[i] !=' ':
        print(arr[i])
    else:
        continue