'''
import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(t):
    m,n,k=map(int,input().split())
    arr=[[0]*m for _ in range(n)]
    for i in range(k):
        x,y=map(int,input().split())
        arr[y][x]=1
    cnt = 0

    def bfs(arr,a,b):
        queue=deque()
        queue.append([a,b])
        arr[a][b]=0
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                    arr[nx][ny]=0
                    queue.append([nx,ny])
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                bfs(arr,i,j)
                cnt+=1
    print(cnt)
'''

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

t=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(t):
    cnt = 0
    m,n,k=map(int,input().split())
    arr=[[0]*m for _ in range(n)]
    for i in range(k):
        x,y=map(int,input().split())
        arr[y][x]=1

    def dfs(arr,x,y):
        arr[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                dfs(arr,nx,ny)
        return


    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                dfs(arr,i,j)
                cnt+=1
    print(cnt)