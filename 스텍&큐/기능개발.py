def solution(progresses, speeds):
    answer = []
    while(len(progresses) != 0):
        sevice = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while(progresses[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            sevice += 1
            if len(progresses) == 0:
                break
        if sevice != 0:
            answer.append(sevice)
    print(answer)
    return answer
