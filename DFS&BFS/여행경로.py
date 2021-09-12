def solution(tickets):
    answer = []
    global vis
    vis = [0 for i in range(len(tickets))]
    global ress
    ress = []
    res = []
    global ticket
    ticket = tickets
    trip('ICN', res, 0)
    # print(sorted(ress))
    ress.sort()
    ress[0].insert(0, 'ICN')
    return ress[0]


def trip(start, res, depth):
    # print('??',res,depth)
    res1 = res.copy()
    if depth == len(ticket):
        # print('fin??????????',res,depth)
        ress.append(list(res))
        return

    for i in range(len(ticket)):
        if ticket[i][0] == start and vis[i] != 1:

            res1.append(ticket[i][1])
            vis[i] = 1
            # print(ticket[i][0],ticket[i][1],depth,vis,res1)
            trip(ticket[i][1], res1, depth+1)
            res1.pop()
            vis[i] = 0
