def solution(answers):
    answer = []
    A = []
    B = []
    C = []
    a = 0
    b = 0
    c = 0
    Ctemp = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    Btemp = [2, 1, 2, 3, 2, 4, 2, 5]
    while(len(answers) >= len(A)):
        for i in range(1, 6):
            A.append(i)
    while(len(answers) >= len(B)):
        for i in range(0, 8):
            B.append(Btemp[i])
    while(len(answers) >= len(C)):
        for i in range(0, 10):
            C.append(Ctemp[i])
    for i in range(len(answers)):
        if answers[i] == A[i]:
            a += 1
        if answers[i] == B[i]:
            b += 1
        if answers[i] == C[i]:
            c += 1
    arr = [a, b, c]
    maxarr = max(arr)
    for i in range(3):
        if maxarr == arr[i]:
            answer.append(i+1)
    # print(A,B,C)
    return sorted(answer)
