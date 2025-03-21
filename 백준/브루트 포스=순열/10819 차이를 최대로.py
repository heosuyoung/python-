n=int(input())
arr=list(map(int,input().split()))
arr.sort()
result=[]
totals=0
visited=[0]*n
def dfs():
    global totals
    if len(result)==n:
        total=0
        for i in range(n-1):
            total += abs(result[i] - result[i + 1])
        totals=max(totals,total)
        return
    for i in range(n):
        if visited[i]!=1:
            visited[i]=1
            result.append(arr[i])
            dfs()
            result.pop()
            visited[i]=0
dfs()
print(totals)

