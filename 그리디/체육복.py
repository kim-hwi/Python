def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = 0
    los = len(lost)
    for lo in lost:
        if lo in reserve:
            reserve[reserve.index(lo)] = -100
            lost[lost.index(lo)] = 100
            los -= 1

    for lo in lost:
        for re in reserve:
            if abs(lo-re) < 2:
                lost[(lost.index(lo))] = 100
                reserve[(reserve.index(re))] = -100
                los -= 1
                break
    answer = n - los
    return answer
