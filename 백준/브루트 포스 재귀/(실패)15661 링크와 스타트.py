n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[0]*n
result=float('inf')

def allright():
    global result
    start, link= 0,0
    for i in range(n):
        for j in range(i+1,n):
            if visited[i] and visited[j]:
                start+=arr[i][j]+arr[j][i]
            elif visited[i]==0 and visited[j]==0:
                link+=arr[i][j]+arr[j][i]
    result = min(result, abs(start-link))



def dfs(cnt,x):
    if cnt > n//2:
        return
    if cnt >=1:
        allright()


    for i in range(x,n):
        visited[i]=1
        dfs(cnt+1,i+1)
        visited[i]=0
dfs(0,0)
print(result)




