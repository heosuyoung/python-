t = int(input())
for _ in range(1,t+1):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    for k in range(m):
        a,b,c=map(int,input().split())
        b = b - 1
        for i in range(1,c+1):
            if 0<=(b-i)<n and 0<=(b+i)<n:
                if arr[b-i]!=arr[b+i]:
                    continue
                else:
                    arr[b-i]=1-arr[b-i]
                    arr[b+i]=1-arr[b+i]
            else:
                break
    print(f'#{_}',*arr)