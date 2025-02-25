n=int(input())
for _ in range(n):
    stack=[]
    arr=input()
    for i in arr:
        if i =='(':
            stack.append(i)
        elif i ==')':
            if stack: #stack에 (가 있다면  (만 append하는 거를 유의
                stack.pop()
            else: #stack에 (가 없다면
                print('NO')
                break #for문 나감
    else:                #break문으로 끝나지 않았을경우
        if not stack: #비어있다면 yes
            print('YES')
        else:
            print('NO')
















