def solution(board, moves):
    count = 0
    res = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                # print(res)
                if len(res) > 0:
                    if res[-1] == board[j][i-1]:
                        count += 2
                        res.pop()
                        board[j][i-1] = 0
                        break

                res.append(board[j][i-1])
                board[j][i-1] = 0

                break
    # print(res)
    return count
