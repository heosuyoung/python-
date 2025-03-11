T=int(input())
for _ in range(1,T+1):
    n=int(input())
    dat=[0]*401
    max=0
    for i in range(n):
        x,y=map(int,input().split())
        tar=0
        if x>y:
            tar=x
            x=y
            y=tar
        if x%2==0:
            x-=1
        if y % 2 == 0:
            y-=1

        for j in range(x,y+1):
            dat[j]+=1
    for i in range(401):
        if dat[i]>max:
            max=dat[i]
    print(f'#{_} {max}')
