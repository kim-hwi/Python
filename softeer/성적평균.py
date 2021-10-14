import math
n, k = map(int, input().split())
student = [int(i) for i in input().split()]
av = [[int(i) for i in input().split()]for j in range(k)]
for i in range(k):
    a = sum(student[av[i][0]-1:av[i][1]]) / (av[i][1]-av[i][0]+1)
    print("{:.2f}".format(a))
