import copy
dix = [0, 1, 1]
diy = [1, 0, 1]


def solution(m, n, board):
    bor = []
    cot = 0

    vis = [[0 for i in range(m)]for j in range(n)]

    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(board[j][i])
        bor.append(temp)
    pop = []

    temp = []
    while temp != bor:
        temp = copy.deepcopy(bor)
        for i in range(n-1):
            for j in range(m-1):
                flag = False
                if bor[i][j] != '-1' and bor[i][j] == bor[i][j+1] and bor[i][j] == bor[i+1][j] and bor[i][j] == bor[i+1][j+1]:
                    pop.append([i, j])
                    pop.append([i+1, j])
                    pop.append([i, j+1])
                    pop.append([i+1, j+1])
        # print(pop)
        for i in pop:
            bor[i[0]][i[1]] = '0'
        # print(pop)
        for i in range(n):
            for j in range(m):
                if bor[i][j] == '0':
                    bor[i].pop(j)
                    bor[i].insert(0, '-1')
                    cot += 1
        pop = []

    answer = cot
    return answer
