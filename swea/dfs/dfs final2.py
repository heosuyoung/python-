map=[
    [0,2,6,3,0,0],
    [2,0,7,4,0,0],
    [6,7,0,0,0,0],
    [3,4,2,0,0,0],
    [0,0,1,0,0,7],
    [0,0,0,0,0,0]
]
used=[0]*6
def dfs(x):
    print(x,end=' ')

    for i in range(len(map)):
        if map[x][i]==0:
            continue
        if used[i]==1:
            continue
        used[i]=1
        dfs(i)
        used[i]=0
dfs(4)