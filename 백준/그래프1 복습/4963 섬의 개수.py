from collections import deque
import sys
input=sys.stdin.readline
dx=[0,0,1,-1,-1,-1,1,1]
dy=[-1,1,0,0,1,-1,1,-1]
def bfs(arr,a,b):
    queue=deque()
    queue.append([a,b])
    arr[a][b]=0
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=h or ny>=w:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=0
                queue.append([nx,ny])
    return
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr=[list(map(int,input().split()))for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                bfs(arr,i,j)
                cnt+=1
    print(cnt)
