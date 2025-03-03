import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

input=sys.stdin.readline

n,m=map(int,input().split())
visited=[0]*(n+1)
# graph=[[0]*(n+1) for _ in range(n+1)]
graph=[[] for _ in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    # graph[a][b]=graph[b][a]=1
    graph[a].append(b)
    graph[b].append(a) #인접행렬은 비효율적 인접리스트로 변경

def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            visited[i]=1
            dfs(i)

cnt=0

for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1

print(cnt)