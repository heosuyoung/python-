n,m=map(int,input().split())
arr=list(map(int,input().split()))
result=[]
arr.sort()
def dfs(x):
    if len(result)==m:
        print(*result)
        return
    for i in range(x,n):
        result.append(arr[i])
        dfs(i+1)
        result.pop()
dfs(0)