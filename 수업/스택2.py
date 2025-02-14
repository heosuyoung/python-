def is_brackets(text):
    stack=[]

    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) ==0

arr = [
    '()()((()))',
    '((()(((()()((()())))'
]

for text in arr:
    if is_brackets(text):
        print(f'{text}는 올바른 괄호식입니다.')
    else:
        print(f'{text}는 올바르지 않은 괄호식 입니다.')