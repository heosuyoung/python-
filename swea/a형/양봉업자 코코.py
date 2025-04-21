from itertools import combinations


def dfs(y, x, cnt, total):
    global max_price, arr, m, n, visited
    # 4개되면 최대값 비교
    if cnt == 4:
        max_price = max(max_price, total)
        return

    # 짝수일때
    if x % 2 == 0:
        direction = even_num_direction
    # 홀수일때
    else:
        direction = odd_num_direction

    # 방향배열 돌기
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, cnt + 1, total + arr[ny][nx])
            visited[ny][nx] = False


def check_T_shape(y, x):
    global max_price, arr, n, m, even_num_direction, odd_num_direction

    # 열의 홀짝에 따라 인접 방향 결정
    if x % 2 == 0:
        directions = even_num_direction
    else:
        directions = odd_num_direction

    neighbors = []
    # 현재 셀(y, x) 주변의 유효한 인접 셀 값 모으기
    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m:
            neighbors.append(arr[ny][nx])

    # 인접 셀이 3개 미만이면 T자 모양 구성 불가
    if len(neighbors) >= 3:
        center = arr[y][x]
        for i, j, k in combinations(range(len(neighbors)), 3):
            total = center + neighbors[i] + neighbors[j] + neighbors[k]
            max_price = max(max_price, total)


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_price = 0
    visited = [[False] * m for _ in range(n)]

    # 홀수 방향배열 (정답 코드와 동일하게 수정)
    odd_num_direction = [(0, -1), (-1, 0), (0, 1), (1, 1), (1, 0), (1, -1)]
    # 짝수 방향배열 (정답 코드와 동일하게 수정)
    even_num_direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1)]

    for y in range(n):
        for x in range(m):
            visited[y][x] = True
            dfs(y, x, 1, arr[y][x])
            visited[y][x] = False
            check_T_shape(y, x)

    print(f'#{tc} {max_price}')