def solution(prices):
    answer = [0 for i in range(len(prices))]
    for A in range(len(prices)):
        count = 0
        for B in range(A+1, len(prices)):
            count += 1
            if prices[A] > prices[B]:
                break
        answer[A] = count
    return answer
