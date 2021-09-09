import itertools


def solution(relation):
    # print(relation)
    ans = [i for i in range(len(relation[0]))]
    count = 0
    print(ans)

    # print(result)
    for num in range(1, len(relation[0])+1):
        result = list(itertools.combinations(ans, num))
        # print(result)
        arr = ['' for i in range(len(relation))]
        for tup in result:

            for tup2 in tup:
                # print(tup2,end=' ')
                for i in range(len(relation)):
                    arr[i] += relation[i][tup2]
            if len(set(arr)) == len(relation):
                print(arr, len(set(arr)), len(relation))
                if tup2 in ans:
                    ans.remove(tup2)
                count += 1
            arr = ['' for i in range(len(relation))]
            # arr.clear()

    #     for tup in range(1,num+1):
    #         print(tup,end=' ')
    #     print()
    #     for i in relation:
    #     ans.append(i[0])
    # print(len(set(ans)))
    return count


arr = [["400", "con", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
    "400", "con", "music", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(arr))