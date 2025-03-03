import sys
from collections import deque
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

visited1=[False]*(n+1) #dfs 방문배열
visited2=[False]*(n+1) #bfs 방문배열

#dfs만들기
def dfs(v):
    visited1[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if visited1[i]==0 and graph[v][i]==1:
            dfs(i)

#bfs만들기
def bfs(v):
    queue=deque([v])
    visited2[v]=1
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if visited2[i]==0 and graph[v][i]==1:
                queue.append(i)
                visited2[i]=1
dfs(v)
print()
bfs(v)