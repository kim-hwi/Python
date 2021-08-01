num = int(input())
arr=[[0,1,1,1,1,1,1,1,1,1] for i in range(101)]
for i in range(1,num):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][j+1]
        elif j == 9:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j+1]
print(sum(arr[num-1]) % 1000000000)
# for i in range(1,num):
#     arr.append(arr[i-1]*2-2*i)
# print(arr[num-1])


