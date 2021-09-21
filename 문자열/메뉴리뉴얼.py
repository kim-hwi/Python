
import itertools
from collections import Counter


def solution(orders, course):
    res = []
    answer = []
    for i in course:
        lis = {}
        for j in range(len(orders)):
            if len(orders[j]) < i:
                continue
            arr = sorted(
                list(map(''.join, itertools.combinations(sorted(orders[j]), i))))
            for ar in arr:
                if ar in lis:
                    lis[ar] = lis[ar]+1
                else:
                    lis[ar] = 1
            # print(lis)
        maxnum = 1
        for li in lis.items():
            maxnum = max(li[1], maxnum)

        if maxnum >= 2:
            for li in lis.items():
                if maxnum == li[1]:
                    res.append(li[0])

        # counter = Counter(lis)
        # print(counter)
        # if len(counter) != 0 and max(counter.values()) != 1:
        #     if max(counter.values())==maxnum:
        #         answer += [f for f in counter if counter[f] == max(counter.values())]

    return sorted(res)
