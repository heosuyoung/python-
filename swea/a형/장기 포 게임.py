'''
먹은 거는 방문 배열에 넣고
방문 배열을 이제 먹지 못함
하지만 넘어갈 수는 있음
1이 있으면 넘어갈수있음 맵을 넘지 않는 다는 가정하여

'''
t=int(input())
for tc in range(1,t+1):
    n=int(input())
    maps=[list(map(int,input().split())) for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    cnt=0 #포 이동 횟수
    result=set() #쫄 먹은 횟수
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    def dfs(starty,startx,cnt):
        if cnt==3:
            return
        for i in range(4):
            for j in range(1,n):
                ny=y+dy[i]*j
                nx=x+dx[i]*j
                if maps[ny][nx]==1:
                    jumpy=ny+dy[i]
                    jumpx=nx+dx[i]
                    if maps[jumpy][jumpx]==0:







    for y in range(n):
        for x in range(n):
            if maps[y][x]==2:
                dfs(y,x,cnt)


    print(f'#{tc} {len(result)}')