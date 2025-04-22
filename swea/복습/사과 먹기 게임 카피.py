from collections import deque
t=int(input())
dy=[0,1,0,-1]
dx=[1,0,-1,0]
for tc in range(1,t+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    apples=[]
    for y in range(n):
        for x in range(n):
            if arr[y][x]!=0:
                apples.append((arr[y][x],y,x))
    apples.sort()
    y,x,dir,total_turns=0,0,0,0

    for _,ay,ax in apples:
        visited=[[[False]*4 for _ in range(n)] for _ in range(n)]
        q=deque([(y,x,dir,0)])
        visited[y][x][dir]=True
        found=False
        while q and not found:
            cy,cx,cd,turns=q.popleft()

            if (cy,cx) == (ay,ax):
                total_turns+=turns
                y,x,dir=cy,cx,cd
                found=True
                break

            ny,nx=cy+dy[cd],cx+dx[cd]
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx][cd]:
                visited[ny][nx][cd]=True
                q.appendleft((ny,nx,cd,turns))

            nd= (cd+1) % 4
            if not visited[cy][cx][nd]:
                visited[cy][cx][nd]=True
                q.append((cy,cx,nd,turns+1))
    print(f'#{tc} {total_turns}')

