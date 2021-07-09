testcase,num = map(int,input().split())
arr = list(map(int,input().split()))
temp = 300000
for i in range(testcase-1):
    for j in range(1,testcase-1):
        for k in range(2,testcase-1):
            arr[i]+arr[j]+arr[k]
print(testcase,num,arr)
