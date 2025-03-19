n,m=map(int,input().split())
arr=list(map(int,input().split()))
result=[]
arr.sort()
def dfs():
    if len(result)==m:
        print(*result)
        return
    prev=0
    for i in range(n):
        if  prev !=arr[i]:
            result.append(arr[i])
            prev = arr[i]
            dfs()
            result.pop()
dfs()