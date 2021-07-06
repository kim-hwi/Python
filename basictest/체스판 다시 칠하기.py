N,M = map(int,input().split())
arr = ["!" for j in range(N)]

temp1 = [["" for j in range(M)] for i in range(N)]

temp2 = [["" for j in range(M)] for i in range(N)]

for i in range(N):
    arr[i] = str(input())

for i in range(N):
    for j in range(M):
        if i % 2 == 0 and j % 2 == 0:
            temp1[i][j] = 'B'
            temp2[i][j] = 'W'
        if i % 2 == 1 and j % 2 == 0:
            temp1[i][j] = 'W'
            temp2[i][j] = 'B'
        if i % 2 == 0 and j % 2 == 1:
            temp1[i][j] = 'W'
            temp2[i][j] = 'B'
        if i % 2 == 1 and j % 2 == 1:
            temp1[i][j] = 'B'
            temp2[i][j] = 'W'

count = N*M
cnt1 = 0
cnt2 = 0
for i in range(0,N-7):
    for j in range(0,M-7):
        for k in range(i,8+i):
            for l in range(j,8+j): 
                if arr[k][l] != temp1[k-i][l-j]:
                    cnt1 += 1
                if arr[k][l] != temp2[k-i][l-j]:
                    cnt2 += 1
        count = min(cnt1,cnt2,count)
        cnt1 = 0
        cnt2 = 0

print(count)
