n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
result=[]

def dfs():
    if len(result)==m:
        print(*result)
        return
    for i in range(n):
        result.append(arr[i])
        dfs()
        result.pop()
dfs()