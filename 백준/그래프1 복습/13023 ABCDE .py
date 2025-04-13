import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
visited=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b) #친구 배열만들어주고
    graph[b].append(a) #인접리스트 만들기
def dfs(x,n):
    if n==5: #depth가 5가 된다면 1출력후 프로그램 종료
        print(1)
        exit()
    visited[x]=1 #방문 표시하고
    for i in graph[x]:
        if not visited[i]:
            dfs(i,n+1) #해당 그래프에서 방문하지 않은게 있다면 depth올리면서 다음 그래프로
    visited[x]=0 #백트래킹
for i in range(n): #모든 그래프 돌아서 depth가 5인거 찾아보기
    vistied=[0]*n
    dfs(i,1)
print(0) #아니면 0