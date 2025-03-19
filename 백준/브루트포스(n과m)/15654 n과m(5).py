n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
result=[]
def dfs():
    if len(result)==m:
        print(*result)
        return
    for i in range(n):
        if arr[i] not in result:
            result.append(arr[i])
            dfs()
            result.pop()
dfs()

        