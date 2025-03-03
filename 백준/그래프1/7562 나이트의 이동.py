import sys
from collections import deque
input=sys.stdin.readline

k=int(input())

dx=[-1,-2,1,2,-1,-2,1,2]
dy=[-2,-1,-2,-1,2,1,2,1]



def bfs():
    while queue:
        x,y=queue.popleft()
        if (x,y) == (c,d):
            return graph[x][y]

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return -1

for _ in range(k):
    l = int(input())
    graph=[[0]*l for _ in range(l)]
    a, b = map(int, input().split())
    queue = deque()

    queue.append((a,b))
    c,d=map(int,input().split())
    if (a,b) ==(c,d):
        print(0)
        continue
    graph[a][b]=0
    print(bfs())

