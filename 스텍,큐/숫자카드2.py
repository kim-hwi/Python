N = int(input())
arr1 = list(map(int,input().split(' ')))
M = int(input())
arr2 = list(map(int, input().split(' ')))
arr3=dict()
for i in arr1:
    try:
        arr3[i] += 1
    except:
        arr3[i] = 1
# print(arr3)
res=[]
for i in arr2:
    try:
        res.append(arr3[i])
    except:
        res.append(0)
# arr3 = set(arr2)
# ans = [0 for i in range(len(arr2))]
# # print( N , arr1)
# # print( M , arr2)
# for i in range(len(arr1)):
#     if arr1[i] in arr3:
#         ans[arr2.index(arr1[i])]+=1
for i in res:
    print(i,end=' ')
        
