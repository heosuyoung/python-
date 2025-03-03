import sys

input=sys.stdin.readline
n,m=map(int,input().split())

graph=[[] for _ in range(n)]
visited=[False]*n
result=False

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,depth):
    global result
    if depth==4:
        result = True #깊이가 4인 노드를 찾아야하는 문제임
        return

    for i in graph[x]:
        if not visited[i]:
            visited[i]=True
            dfs(i,depth+1)
            visited[i]=False #한 경로를 탐색한 후에 방문 기록을 지워줘야 모든 노드 탐색가능
for i in range(n):
    visited[i]=True
    dfs(i,0)
    visited[i]=False #만약 result True가 되면 탐색 종료
    if result:
        break
if result:
    print(1)
else:
    print(0)