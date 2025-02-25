T=int(input())
for _ in range(1,T+1):
    N,M=map(int,input().split())
    ans=list(map(int,input().split()))
    info=[list(map(int,input().split())) for _ in range(N)]
    scores=[]
    for i in range(N):
        cnt = 0
        seq = 0
        for j in range(M):
            if info[i][j] == ans[j]:
                seq+=1
                cnt+=seq
            else:
                seq=0
        scores.append(cnt)
    result=max(scores)-min(scores)
    print(f'#{_} {result}')