num = int(input())
arr =[0 for i in range(num)]
red = 0
blue = 0
for i in range(num):
    arr[i] = list(map(int, input().split(' ')))

def fun (nownum,x,y):
    global red
    global blue
    if nownum == 1:
        if arr[x][y] == 1:
            red += 1
        if arr[x][y] == 0:
            blue += 1
        # print('in',nownum,x,y,arr[x][y])
        return 1
    for i in range(x,x+nownum-1):
        for j in range(y,y+nownum-1):
            if arr[i][j] != arr[i][j+1] or arr[i][j] != arr[i+1][j] or arr[i][j] != arr[i+1][j+1]:
                return fun(int(nownum/2), x, y) + fun(int(nownum/2), int(nownum/2)+x, y) + fun(int(nownum/2), x, int(nownum/2)+y) + fun(int(nownum/2), int(nownum/2)+x, int(nownum/2)+y)
    if arr[x][y] == 1:
        red += 1
    if arr[x][y] == 0:
        blue += 1
    # print('out', nownum, x, y, arr[x][y])
    return 1

fun(num, 0, 0)

print(blue)
print(red)
