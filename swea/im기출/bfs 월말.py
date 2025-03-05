def bfs(y,x):
    q=[]
    visited=[[0]*N for _ in range(N)]
    q.append((x,y))
    visited[y][x]=1

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        ty,tx=q.pop(0)
        if arr[tx][ty]==3:
            return visited[ty][tx]
        for i in range(4):
            k=1
            if arr[ty][tx]==4:
                k=2
            nx=tx+dx[i]*k
            ny=ty+dy[i]*k

            if 0<=ny<N and 0<=nx<N and arr[ny][nx]!=1 and visited[ny][nx]==0:
                q.append((ny,nx))
                visited[ny][nx] =visited[ty][tx]+1

    return -1

def find_start():
    for y in range(N):
        for x in range(N):
            if arr[y][x] ==2:
                return y,x

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    sty,stx=find_start()
    ret=bfs(sty,stx)
    print(f'#{tc} {ret}')