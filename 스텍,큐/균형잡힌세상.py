arr = str(input())
# print(type(arr),len(arr))
while(len(arr) != 0):
    st = []
    if len(arr) == 1 and arr[0] == '.':
        exit(0)
    for i in arr:
        if i == '(':
            st.append('(')
        elif i == '[':
            st.append('[')
        elif i == ')':
            if len(st) == 0:
                st.append(-1)
                break
            elif st[-1] == '(':
                st.pop()
            elif st[-1] == '[':
                st.append(-1)
                break
            elif st[-1] == ']':
                st.append(-1)
                break
        elif i == ']':
            if len(st) == 0:
                st.append(-1)
                break
            elif st[-1] == '[':
                st.pop()
            elif st[-1] == '(':
                st.append(-1)
                break
            elif st[-1] == ')':
                st.append(-1)
                break
    if -1 in st or len(st) != 0:
        print('no')
    else:
        print('yes')
    arr = str(input())
    
