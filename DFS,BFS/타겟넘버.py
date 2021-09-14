def solution(numbers, target):
    global arr
    global tar
    global answer
    arr = numbers
    tar = target
    answer = []

    targetsum(0, 0)

    return len(answer)


def targetsum(num, res):
    if num == len(arr):
        if res == tar:
            answer.append(1)
            # print(answer)
        return
    targetsum(num+1, res+arr[num])
    targetsum(num+1, res-arr[num])
