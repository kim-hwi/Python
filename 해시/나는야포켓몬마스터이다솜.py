D,Q = input().split()
dogamnum = {}
dogamstr = {}
for i in range(int(D)):
    name = input()
    dogamstr[name] = i+1
    dogamnum[i+1] = name
for i in range(int(Q)):
    qu = input()
    try:
        qu=int(qu)
        print(dogamnum[qu])
    except:
        print(dogamstr[qu])
# print(dogamstr)
# print(dogamnum)
