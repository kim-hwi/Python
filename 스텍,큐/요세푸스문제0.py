# 1 2 3 4 5 6 7
# 1 2 4 5 6 7
# 1 2 4 5 7
# 1 4 5 7

N,k = map(int,input().split())

arr = [i for i in range(1,N+1)]
num=0
print('<',end='')
while len(arr)  != 1:
    num+=k-1
    # print(arr,num,len(arr))
    if len(arr)<num+1:
        num=num%len(arr)
    
    # print(arr,num)
    print(arr.pop(num),end=', ')

print(arr.pop(),'>',end='',sep='')

