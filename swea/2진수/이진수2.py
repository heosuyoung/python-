t=int(input())
for _ in range(1,t+1):
    n=float(input())
    a = 0.5
    sum = ''
    while n>0:
        if len(sum)>12:
            sum='overflow'
            break
        if n>=a:
            sum+='1'
            n-=a
            a/=2
        else:
            a/=2
            sum+='0'
    print(f'#{_} {sum}')
