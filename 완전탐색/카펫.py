def solution(brown, yellow):
    answer = []
    for i in range(3, int(brown/2)):
        A = i
        B = int(brown/2)+2-i
        # print(A,B)
        if A >= B and A*B == brown+yellow:
            answer = [A, B]
    return answer
