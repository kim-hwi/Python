def solution(rows, columns, queries):
    num = 0
    board = [[i+1+columns*j for i in range(columns)]for j in range(rows)]
    ans = []

    for q in queries:

        temp = []

        for k in range(abs(q[3]-q[1])):
            temp.append(board[q[0]-1][q[1]+k-1])

        for k in range(abs(q[2]-q[0])):
            temp.append(board[q[0]+k-1][q[3]-1])

        for k in range(abs(q[3]-q[1])):
            temp.append(board[q[2]-1][q[3]-k-1])

        for k in range(abs(q[2]-q[0])):

            temp.append(board[q[2]-k-1][q[1]-1])

        ans.append(min(temp))

        temp.insert(0, temp.pop())

        print()
        for k in range(abs(q[3]-q[1])):
            board[q[0]-1][q[1]+k-1] = temp.pop(0)

        for k in range(abs(q[2]-q[0])):
            board[q[0]+k-1][q[3]-1] = temp.pop(0)

        for k in range(abs(q[3]-q[1])):
            board[q[2]-1][q[3]-k-1] = temp.pop(0)

        for k in range(abs(q[2]-q[0])):
            board[q[2]-k-1][q[1]-1] = temp.pop(0)

    print(ans)

    return ans
