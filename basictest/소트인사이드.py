testcase = str(input())

arr = [0 for i in range(len(testcase))]

for i in range(len(testcase)):
    arr[i] = int(testcase[i])

arr.sort(reverse=1)

for i in range(len(testcase)):
    print(arr[i], end='')
