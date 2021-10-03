from heapq import *          

def solution(scoville, K):
    heapify(scoville)
    count=0
    while scoville[0] < K and len(scoville) > 1:
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville,a+b*2)
        count+=1
        
    if scoville[0] < K:
        count=-1
        
    # print(count)
    answer = count
    return answer