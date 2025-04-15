import sys
from collections import deque
m,n=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt = 0

queue=deque()

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            queue.append((i,j))

while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==0:
                arr[nx][ny]=arr[x][y]+1
                queue.append((nx,ny))
result=0
for row in arr:
    if 0 in row:
        print(-1)
        break
    result=max(result,max(row))
else: # for-else문으로 for 문이 break없이 끝났냐? 그러면 else문
    print(result-1) #시작이 1이니깐