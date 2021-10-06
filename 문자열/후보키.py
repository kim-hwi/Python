import itertools


def solution(relation):
    ans = []
    sch = [i for i in range(len(relation[0]))]
    for i in range(1, len(relation[0])+1):
        li = list(map(list, itertools.combinations(sch, i)))
        for j in li:
            temp = []
            for q in relation:
                temp2 = ''
                for l in j:
                    temp2 += q[l]
                temp.append(temp2)

            lenli = len(set(temp))
            if lenli == len(temp):
                flag = True
                for an in ans:
                    # print(an,j,ans)
                    # print(an,sorted(list(set(an)&set(j))))
                    if an == sorted(list(set(an) & set(j))):
                        flag = False
                        break
                if flag == True:
                    ans.append(j)
    return len(ans)
