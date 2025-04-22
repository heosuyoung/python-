
def dfs(y,x,cnt):
    if cnt==3:
        return
    for i in range(4):
        for jump in range(1,n):
            ny,nx=y+dy[i]*jump,x+dx[i]*jump
            if not (0<=nx<n and 0<=ny<n ):
                break
            if arr[ny][nx]==1:
                for jump2 in range(1,n):
                    ny2,nx2=ny+dy[i]*jump2,nx+dx[i]*jump2
                    if not(0<=nx2<n and 0<=ny2<n):
                        break
                    if arr[ny2][nx2] == 0:
                        dfs(ny2,nx2,cnt+1)
                    elif arr[ny2][nx2] ==1:
                        result.add((ny2,nx2))
                        arr[ny2][nx2]=0
                        dfs(ny2,nx2,cnt+1)
                        arr[ny2][nx2]=1
                        break
                break


t=int(input())
dy=[-1,1,0,0]
dx=[0,0,-1,1]
for tc in range(1,t+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    result=set()
    for y in range(n):
        for x in range(n):
            if arr[y][x]==2:
                arr[y][x]=0
                dfs(y,x,0)
    print(f'#{tc} {len(result)}')