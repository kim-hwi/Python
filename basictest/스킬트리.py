def solution(skill, skill_trees):
    s = skill
    st = skill_trees
    answer = 0

    for i in range(len(st)):
        flag = False
        # print(s)
        qu = list(s)
        us = list(st[i])
        while qu and us:
            temp = us.pop(0)
            if temp in qu:
                if qu.index(temp) == 0:
                    qu.pop(0)
                else:
                    flag = True
                    break
        if flag == True:
            continue
        answer += 1

    return answer
