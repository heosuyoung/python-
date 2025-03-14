
def dfs(x,sum_v,cnt):
    global min_v
    if sum_v>=min_v:
        return
    if cnt==n-1:
        if arr[x][0]:
            sum_v+=arr[x][0]
            min_v=min(min_v,sum_v)

    for i in range(1,n):
        if arr[x][i]==0:
            continue
        if visited[i]==1:
            continue
        visited[i]=1
        dfs(i,sum_v+arr[x][i],cnt+1)
        visited[i]=0
T=int(input())
for _ in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    min_v=float('inf')
    visited=[0]*n
    visited[0]=1
    dfs(0,0,0)
    print(f'#{_} {min_v}')