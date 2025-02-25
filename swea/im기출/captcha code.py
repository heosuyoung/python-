T=int(input())
for _ in range(1,T+1):
    N,K=map(int,input().split())
    sample=list(map(int,input().split()))
    password=list(map(int,input().split()))

    pass_num=0
    flag=0

    for i in sample:
        if i == password[pass_num]:
            pass_num +=1
            if pass_num == K:
                flag=1
                break
    print(f'#{_} {flag}')
