n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
result=[]

def dfs(x):
    if len(result)==m:
        print(*result)
        return
    prev=0
    for i in range(x,n):
        if prev !=arr[i]:
            result.append(arr[i])
            prev=arr[i]
            dfs(i)
            result.pop()
dfs(0)