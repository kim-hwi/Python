teatcase = int(input())
arr = [[int(input()), 0, 0] for i in range(teatcase)]

def fun() :
        
    if teatcase == 1:
        arr[0][1] = arr[0][0]
        return
    if teatcase == 2:
        arr[1][1] = arr[0][0]+arr[1][0]
        return
    if teatcase == 3:
        arr[2][1] = max( arr[0][0]+arr[1][0] , arr[0][0]+arr[2][0] , arr[1][0]+arr[2][0])
        return
    arr[0][1] = arr[0][0]
    arr[0][2] = 1
    arr[1][1] = arr[1][0]+arr[0][1]
    arr[1][2] = 2

    for i in range(2, teatcase):
        if arr[i-1][2] == 2:

            if arr[i-1][1] < arr[i][0]+arr[i-1][0] :
                arr[i][1] = arr[i][0]+arr[i-1][0]+arr[i-3][1]
                arr[i][2] = 2
                arr[i-1][2] = 1
                arr[i-2][2] = 0

            elif arr[i-1][1] <= arr[i][0]+arr[i-2][1]:
                arr[i][1] = arr[i][0]+arr[i-2][1]
                arr[i-1][2] = 0
                arr[i][2] = 1
            elif arr[i-1][1] > arr[i][0]+arr[i-1][0]:
                arr[i][1] = arr[i-1][1]
                arr[i][2] = 0

        # 1 2 2
        # 1 3 5
        # 1 2 3 4

        # 1 2 1
        # 5 6 8
        # 5 1 3

        elif arr[i-1][2] == 1:
            arr[i][1] = arr[i][0]+arr[i-1][1]
            arr[i][2] = 2

        else:
            arr[i][1] = arr[i][0]+arr[i-1][1]
            arr[i][2] = 1
    
fun()
print(arr)
print(arr[teatcase-1][1])
