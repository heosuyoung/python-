T=int(input())

for i in range(1,T+1):
    string=list(input())
    stack = []
    for char in string:
        if stack and char==stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    print(f'#{i} {len(stack)}')