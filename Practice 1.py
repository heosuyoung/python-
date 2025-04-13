import heapq

turn_cnt=(
    (0,2,1,1),
    (2,0,1,1),
    (1,1,0,2),
    (1,1,2,0),
)
ydir=(-1,1,0,0)
xdir=(0,0,-1,1)

def dijkstra(y,x):
    dist=[]
    for k in range(K+1):
        dist.append([[21e8 for _ in range(n)] for _ in range(n)])
    pq=[]
    heapq.heappush(pq,(0,k,y,x,0)) # (cost, 남은부수기, y, x, 방향)

    while len(pq):
        cost,cnt,y,x,dir=heapq.heappop(pq)
        for i in range(4):
            ny=y+ydir[i]
            nx=x+xdir[i]
            nc=cost+turn_cnt[dir][i]+1

            if ny<0 or nx<0 or ny>=n or nx>=n:
                continue
            if dist[cnt][ny][nx]<=nc:
                continue
            if board[ny][nx]=='T' and cnt==0:
                continue
            if board[ny][nx]=='T'and cnt>0:
                heapq.heappush(pq,(nc,cnt-1,ny,nx,i))
            else:
                heapq.heappush(pq,(nc,cnt,ny,nx,i))
            dist[cnt][ny][nx]=nc
    res=21e8
    for i in range(k+1):
        res=min(res,dist[i][dy][dx])
    if res==21e8:
        return -1
    return res




t=int(input())
for _ in range(1,t+1):
    n,K=map(int,input().split())
    board=[list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                sy,sx=i,j
            elif board[i][j] == 'Y':
                dy,dx=i,j

    print(f'#{_} {dijkstra(sy,sx)}')