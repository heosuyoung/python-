data=input()
stack=[]
ans=''
check=False

for d in data:
    if d =='<':
        check=True
        for _ in range(len(stack)):
            ans += stack.pop()
    stack.append(d)

    if d =='>':
        check=False
        for _ in range(len(stack)):
            ans +=stack.pop(0)

    if d ==' ' and check == False:
        stack.pop()
        for _ in range(len(stack)):
            ans+=stack.pop()
        ans+=" "
if stack:
    for _ in range(len(stack)):
        ans += stack.pop()
print(ans)

