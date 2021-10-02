from heapq import *

a=[1,2,3,4,5]
heap=[]

for i in a:
    heappush(heap,[-i,i])
heapify(a)
while len(heap) != 0:
    print(heappop(heap)[1])
print(a[3])
