''' 인접리스트
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)
cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1
print(cnt)
'''
n,m=map(int,input().split()) #인접행렬
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
visited=[0]*(n+1)
def dfs(v):
    visited[v]=1
    for i in range (1,n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(i)
cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1
print(cnt)