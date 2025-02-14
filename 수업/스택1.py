def push(stack, item):  # stack에 추가한다 stack을 매개변수로
    stack.append(item)  # stack의 데이터가 수정이 되기 떄문에 지역변수


def pop_stack(stack):
    if stack:  # 스택이 비어있지 않으면
        return stack.pop()  # 반환값이 있어서 return함
    return None  # 스택이 비어있으면 None 반환

stack=[]
push(stack,1)
push(stack,2)
push(stack,3)
print(stack)

a=pop_stack(stack)
b=pop_stack(stack)
c=pop_stack(stack)

print(a)
print(b)
print(c)
print(stack)




