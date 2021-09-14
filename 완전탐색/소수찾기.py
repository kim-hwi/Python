import math
import itertools


def solution(numbers):
    count = 0
    arr = str(numbers)
    print(arr)
    arr2 = []
    for i in range(1, len(numbers)+1):
        arr2 += list(map(''.join, itertools.permutations(arr, i)))
    arr2 = map(int, arr2)
    arr2 = set(arr2)
    arr2 = list(arr2)

    for num in arr2:
        if pri(int(num)) == True:
            count += 1
            print(num)

    # print(arr2)

    return count


def pri(X):
    for i in range(2, int(math.sqrt(X))+1):
        if X % i == 0:
            return False
    if X == 0 or X == 1:
        return False
    return True
