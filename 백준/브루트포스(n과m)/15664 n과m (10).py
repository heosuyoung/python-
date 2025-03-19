n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
result=[]
visited=[0]*(n+1)
def dfs(x):
    if len(result)==m:
        print(*result)
        return
    prev=0
    for i in range(x,n):
        if visited[i] !=1 and prev !=arr[i]:
            result.append(arr[i])
            visited[i]=1
            prev=arr[i]
            dfs(i+1)
            visited[i]=0
            result.pop()
dfs(0)