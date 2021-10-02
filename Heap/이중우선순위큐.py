import heapq


def solution(operations):
    print(operations)
    heap1 = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(heap1, int(i[2:]))
        if i[0] == 'D':

            if len(heap1) == 0:
                continue
            if i[2:] == '-1':
                heapq.heappop(heap1)

            if i[2:] == '1':
                temp = []
                while len(heap1) > 1:
                    heapq.heappush(temp, heapq.heappop(heap1))
                heap1 = temp.copy()
    answer = [0, 0]
    if len(heap1) == 0:
        answer = [0, 0]
    elif len(heap1) == 1:
        answer[0] = heapq.heappop(heap1)
        answer[1] = answer[0]
    elif len(heap1) > 1:
        answer[1] = heapq.heappop(heap1)
        while len(heap1) > 1:
            heapq.heappop(heap1)
        answer[0] = heapq.heappop(heap1)
    return answer
