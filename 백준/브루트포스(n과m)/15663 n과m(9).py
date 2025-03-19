n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
result=[]
visited=[0]*(n+1)
def dfs():
    if len(result)==m:
        print(*result)
        return
    pre=0 #이전에 들어왔던건지 확인하는 용
    for i in range(len(arr)):
        if visited[i]==0 and pre != arr[i]: #확인
            visited[i]=1
            result.append(arr[i])
            pre=arr[i]  #그 값을 바로 넣어주고
            dfs()
            result.pop()
            visited[i]=0


dfs()
