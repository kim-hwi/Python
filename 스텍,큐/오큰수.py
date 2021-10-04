N = int(input())
st=[]
res = [-1 for i in range(N)]
loc =0
board = [int(num) for num in input().split()]
# print(board)
st.append(0)
i=1
while st and i<N:
    while st and board[i] > board[st[-1]]:
        res[st[-1]] = board[i]
        st.pop()
    st.append(i)
    i+=1
    
for l in res:
    print(l,end=' ')