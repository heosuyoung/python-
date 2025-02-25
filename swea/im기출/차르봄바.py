T=int(input())
for _ in range (1,T+1):
    n,p=map(int,input().split())
    maps=[list(map(int,input().split())) for _ in range(n)]
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    result=0
    for x in range(n):
        for y in range(n):
            s = maps[x][y]
            for i in range(4):
                for k in range (1,p+1):
                    nx=x+dx[i]*k
                    ny=y+dy[i]*k
                    if 0<=nx<n and 0<=ny<n:
                        s+=maps[nx][ny]
            result=max(result,s)
    print(f'#{_} {result}')