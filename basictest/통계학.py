case = int(input())
arr = [0 for i in range(case)]
arr2 = [0 for i in range(case)]
ma = 0
for i in range(case):
    temp = int(input())
    if temp in arr:
        arr2[arr.index(temp)]+=1
    arr[i] = temp
    ma +=arr[i]
arr3 =[]
for i in range(case):
    if arr2[i] == max(arr2):
        arr3.append(arr[i])
arr3.sort()
if len(arr3) > 1:
    fre = arr3[1]
else:
    fre = arr3[0]
arr.sort()
ma = ma / case
mid = arr[int((case-1)/2)]

print(round(ma))
print(mid)
print(fre)
print(max(arr)-min(arr))
