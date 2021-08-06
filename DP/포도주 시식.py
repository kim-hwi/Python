teatcase = int(input())
arr = [[int(input()), 0, 0,0,0] for i in range(teatcase)]




def fun() :
        
    
    arr[0][4] = arr[0][0]
    if teatcase == 1:
        return
    arr[1][1] = arr[0][0]+arr[1][0]
    arr[1][4] = arr[1][1]
    if teatcase == 2:
        return
    arr[2][1] = arr[0][0]+arr[1][0]
    arr[2][2] = arr[1][0]+arr[2][0]
    arr[2][3] = arr[0][0]+arr[2][0] 
    arr[2][4] = max(arr[2][1],arr[2][2],arr[2][3])
    if teatcase == 3:
        return

    for i in range(3, teatcase):
        temp = i%3
        if temp == 1:
            arr[i][1] = arr[i-1][1]+arr[i][0]
            arr[i][2] = arr[i-1][2]+arr[i][0]
            arr[i][3] = arr[i-1][3]
        if temp == 2:
            arr[i][1] = arr[i-1][1]
            arr[i][2] = arr[i-1][2]+arr[i][0]
            arr[i][3] = arr[i-1][3]+arr[i][0]
        if temp == 0:
            arr[i][1] = arr[i-1][1]+arr[i][0]
            arr[i][2] = arr[i-1][2]
            arr[i][3] = arr[i-1][3]+arr[i][0]

        arr[i][4] = max(arr[i-1][4],
                        arr[i-3][4] + arr[i-1][0] + arr[i][0], 
                        arr[i-2][4] + arr[i][0])
        # 1 2 2
        # 1 3 5
        # 1 2 3 4

        # 1 2 1
        # 5 6 6 6 9 12
        # 3 3 0 0 3 3

fun()    
print(arr[teatcase-1][4])

