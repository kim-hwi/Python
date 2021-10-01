def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [
        2, 0], 8: [2, 1], 9: [2, 2], '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    l = '*'
    r = '#'
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            l = num
        if num == 3 or num == 6 or num == 9:
            answer += 'R'
            r = num
        if num == 2 or num == 5 or num == 8 or num == 0:
            tar = dic[num]
            right = dic[r]
            left = dic[l]
            if abs(tar[0]-right[0])+abs(tar[1]-right[1]) > abs(tar[0]-left[0])+abs(tar[1]-left[1]):
                answer += 'L'
                l = num
            elif abs(tar[0]-right[0])+abs(tar[1]-right[1]) < abs(tar[0]-left[0])+abs(tar[1]-left[1]):
                answer += 'R'
                r = num
            else:
                if hand == 'left':
                    answer += 'L'
                    l = num
                else:
                    answer += 'R'
                    r = num

    return answer
