def solution(bridge_length, weight, truck_weights):
    bridge=[0 for i in range(bridge_length)]
    count=0
    Sum=0
    for i in truck_weights:
        # print(bridge,Sum)
        Sum-=bridge.pop(0)
        while (Sum+i>weight):
            # print('in',bridge,Sum)
            count+=1
            bridge.append(0)
            Sum-=bridge.pop(0)
        bridge.append(i)
        Sum+=i
        
        
        count+=1
        
    count+=bridge_length
        
    return count