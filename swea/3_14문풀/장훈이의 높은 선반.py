T=int(input())
for _ in range(1,T+1):
    n,b=map(int,input().split())
    result=float('inf')
    arr=list(map(int,input().split()))
    for tar in range(1,1<<n):
        s = 0
        #공집합 필요없으므로 1부터
        for i in range(n):
            if tar & 0x1:
                s+=arr[i]
            tar>>=1
            if s>=b:
                diff=s-b
                result=min(result,diff)
    print(f'#{_} {result}')


