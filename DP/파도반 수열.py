testcase=int(input())
arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
case = [int(input()) for i in range(testcase)]

big = max(case)

if(big>9):
    for i in range(10,big):
        
        arr.append(arr[i-1]+arr[i-5])
        # print(arr[i-1],arr[i-6])

for i in range(testcase):
    print(arr[case[i]-1])
# print(arr)