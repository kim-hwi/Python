def solution(lottos, win_nums):
    lot = set(lottos)
    win = set(win_nums)
    ok = lot & win
    sung = lottos.count(0)
    tal = len(ok)
    ans1 = 7-tal-sung
    ans2 = 7-tal
    if ans2 > 6:
        ans2 = 6
    if ans2 < 1:
        ans2 = 1
    if ans1 > 6:
        ans1 = 6
    if ans1 < 1:
        ans1 = 1
    answer = [ans1, ans2]
    return answer
