def solution(s):
    ans = ''
    numlist = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']
    temp = ''
    for st in s:

        if st >= '0' and st <= '9':
            ans += st
        else:
            temp += st
        if temp in numlist:
            ans += str(numlist.index(temp))
            temp = ''

    # print(ans)
    answer = int(ans)
    return answer
