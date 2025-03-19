n,m=map(int,input().split())
arr=[]
visited=[0]*(n+1)
def dfs(x):
    if len(arr)==m:
        print(*arr)
        return
    for i in range(x,n+1):
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)