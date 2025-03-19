n,m=map(int,input().split())
arr=[]
def dfs(x):
    if len(arr)==m:
        print(*arr)
        return
    for i in range(x,n+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
dfs(1)
