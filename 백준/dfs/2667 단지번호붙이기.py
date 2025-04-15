'''

import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().strip())) for _ in range(n)]
result=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt = 0

def dfs(x,y):
    global cnt
    arr[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
            arr[nx][ny]=0
            cnt+=1
            dfs(nx,ny)
    return

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            cnt=1
            dfs(i,j)
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)
'''
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().strip())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
result=[]
def bfs(arr,a,b):
    cnt=1
    queue=deque()
    arr[a][b]=0
    queue.append((a,b))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                arr[nx][ny]=0
                cnt+=1
                queue.append((nx,ny))
    return cnt
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            size=bfs(arr,i,j)
            result.append(size)
result.sort()
print(len(result))
for i in result:
    print(i)



