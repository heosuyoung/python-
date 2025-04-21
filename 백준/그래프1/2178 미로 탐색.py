import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))

'''
n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

stack=[(0,0)]
while stack:
    x,y=stack.pop()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
            maps[nx][ny]=maps[x][y]+1
            stack.append((nx,ny))
print(maps[n-1][m-1])
'''