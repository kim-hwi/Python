import sys
n, m = map(int, input().split())
st = [0 for i in range(100)]
err = [0 for i in range(100)]
start = 0
for i in range(n):
    loc, spp = map(int, input().split())
    for j in range(start, start+loc):
        st[j] = spp
    start = loc+start
# print(st)
start = 0
for i in range(m):
    loc, spp = map(int, input().split())
    for j in range(start, start+loc):
        err[j] = spp
    start = loc+start
# print(err)

res = 0
for i in range(100):
    if st[i] < err[i]:
        res = max(err[i]-st[i], res)
print(res)
