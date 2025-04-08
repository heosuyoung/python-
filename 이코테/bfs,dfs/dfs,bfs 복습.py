''' 팩토리얼


def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)


print(factorial_iterative(5))
print(factorial_recursive(5))
'''

'''
#유클리드 호재법
def gcd(a,b):
    if a % b==0:
        return b
    else:
        return gcd(b, a%b)


print(gcd(192,162))


#dfs

def dfs(graph,v,visited):
    visited[v]=1
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[0]*9
dfs(graph,1,visited)


from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=1
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if visited[i]!=1:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[0]*9
bfs(graph,1,visited)


#얼음 얼리기 dfs
n,m=map(int,input().split())
ice=[list(map(int,input())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt=0

def dfs(x,y):
    if 0<=x<n and 0<=y<m:
        if ice[x][y]==0:
            ice[x][y]=1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs(nx,ny)
            return True
        return False


for i in range(n):
    for j in range(m):
        if dfs(i,j):
            cnt+=1
print(cnt)


from collections import deque

n,m=map(int,input().split())
ice=[list(map(int,input())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]
cnt=0

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    ice[x][y]=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if ice[nx][ny]==0:
                    ice[nx][ny]=1
                    queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if ice[i][j]==0:
            bfs(i,j)
            cnt+=1
print(cnt)
'''
from collections import deque

n,m=map(int,input().split())
maps=[list(map(int,input())) for _ in range(n)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    queue.append((nx,ny))
    return maps[n-1][m-1]

print(bfs(0,0))
