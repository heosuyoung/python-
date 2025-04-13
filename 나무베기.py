import heapq

turn_cnt = (
    #    상 하 좌 우
    (0, 2, 1, 1),  # 상
    (2, 0, 1, 1),  # 하
    (1, 1, 0, 2),  # 좌
    (1, 1, 2, 0)  # 우
)
ydir = (-1, 1, 0, 0)
xdir = (0, 0, -1, 1)


def dijkstra(y, x):
    dist = []
    for k in range(K + 1):
        dist.append([[21e8 for _ in range(N)] for _ in range(N)])
    pq = []
    heapq.heappush(pq, (0, K, y, x, 0))

    while len(pq):
        cost, cnt, y, x, dir = heapq.heappop(pq)
        # print(y, x, dir, cnt, cost)

        for i in range(4):
            ny = y + ydir[i]
            nx = x + xdir[i]
            nc = cost + turn_cnt[dir][i] + 1

            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if dist[cnt][ny][nx] <= nc:
                continue
            if board[ny][nx] == 'T' and cnt == 0:
                continue
            if board[ny][nx] == 'T' and cnt > 0:
                heapq.heappush(pq, (nc, cnt - 1, ny, nx, i))
            else:
                heapq.heappush(pq, (nc, cnt, ny, nx, i))
            dist[cnt][ny][nx] = nc
    res = 21e8
    for i in range(K + 1):
        res = min(res, dist[i][dy][dx])
    if res == 21e8:
        return -1
    return res


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                sy, sx = i, j
            elif board[i][j] == 'Y':
                dy, dx = i, j

    print(f"#{tc} {dijkstra(sy, sx)}")