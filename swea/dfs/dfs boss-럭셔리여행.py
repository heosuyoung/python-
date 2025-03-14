n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
a,b,=map(int,input().split())

max_s=0
min_s=float('inf')
visited=[0]*(n+1)
def dfs(x,cnt):
    global max_s
    global min_s
    if x==b:
        max_s=max(max_s,cnt)
        min_s=min(min_s,cnt)
        return
    #visited[x]==1
    for i in range(n):
        if arr[x][i]==0:
            continue

        if visited[i]==1:
            continue
        visited[i]=1
        dfs(i,cnt+arr[x][i])
        visited[i]=0
visited[a]=1
dfs(a,0)
print(min_s)
print(max_s)