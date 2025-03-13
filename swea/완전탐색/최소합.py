T=int(input())

def dfs(y,x,sum_v):
    global min_sum
    if y==n-1 and x==n-1:
       min_sum= min(min_sum,sum_v)

    if sum_v>=min_sum:
        return
    if x<n-1:
        dfs(y,x+1,sum_v+maps[y][x+1])

    if y<n-1:
        dfs(y+1,x,sum_v+maps[y+1][x])


for _ in range(1,T+1):
    n=int(input())
    maps=[list(map(int,input().split())) for _ in range(n)]
    min_sum=float('inf')
    dfs(0,0,maps[0][0])
    print(f'#{_} {min_sum}')