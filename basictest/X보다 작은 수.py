testcase, num = map(int,input().split())
numlist = list(map(int,input().split()))
for i in range(0,testcase):
    if numlist[i] > num:
        print(numlist[i],end=" ")