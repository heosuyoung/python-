a,b=map(int,input().split())
map=[
    [0,2,6,3,0,0],
    [2,0,7,4,0,0],
    [6,7,0,0,0,0],
    [3,4,2,0,0,0],
    [0,0,1,0,0,7],
    [0,0,0,0,0,0]
]
max_s=0
min_s=float('inf')
used=[0]*6
def dfs(x,cnt):
    global max_s
    global min_s
    if x==b:
        max_s=max(max_s,cnt)
        min_s=min(min_s,cnt)
        return max_s,min_s
    for i in range(len(map)):
        if map[x][i]==0:
            continue
        if used[i]==1:
            continue
        used[i]=1
        dfs(i,cnt+map[x][i])
        used[i]=0
dfs(a,0)
print(max_s)
print(min_s)
