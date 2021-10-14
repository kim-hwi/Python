import itertools



def check(ar, n, m, k):
    num = 0
    start = 0
    for i in range(k):
        wei = 0
        temp = 0

        while wei <= m:
            wei += ar[start]
            temp = start
            start += 1
            if start >= n:
                start = 0
        if temp >= n:
            temp = 0
        start = temp
        wei -= ar[temp]
        num += wei
    return num


res = []
n, m, k = map(int, input().split())
arr = [int(i) for i in input().split()]
board = list(map(list, itertools.permutations(arr, n)))

for i in range(len(board)):
    res.append(check(board[i], n, m, k))
print(min(res))
