import copy

# 방향: 우, 하, 좌, 상
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def simulate(start_y, start_x, start_dir, field, max_day):
    n = len(field)
    arr = copy.deepcopy(field)
    plant_count = [[0]*n for _ in range(n)]
    y, x, d = start_y, start_x, start_dir
    day = 1
    harvest = 0

    while day <= max_day:
        # 수확
        if arr[y][x] not in (0, 1) and day >= arr[y][x]:
            harvest += 1
            arr[y][x] = 0
        # 씨앗 심기
        elif arr[y][x] == 0:
            movable = False
            for i in [(d+1)%4, d, (d+3)%4, (d+2)%4]:
                ny, nx = y + DIRECTIONS[i][0], x + DIRECTIONS[i][1]
                if 0 <= ny < n and 0 <= nx < n:
                    if arr[ny][nx] == 0 or (arr[ny][nx] != 1 and day >= arr[ny][nx]):
                        movable = True
                        break
            if movable:
                plant_count[y][x] += 1
                arr[y][x] = day + 4 + plant_count[y][x]

        # 밤: 이동
        moved = False
        for i in [(d+1)%4, d, (d+3)%4, (d+2)%4]:
            ny, nx = y + DIRECTIONS[i][0], x + DIRECTIONS[i][1]
            if 0 <= ny < n and 0 <= nx < n:
                if arr[ny][nx] == 0 or (arr[ny][nx] != 1 and day >= arr[ny][nx]):
                    y, x, d = ny, nx, i
                    moved = True
                    break
        # 이동 실패 시 위치 유지
        day += 1

    return harvest


t = int(input())
for tc in range(1, t+1):
    n, d = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    max_result = 0

    for y in range(n):
        for x in range(n):
            if field[y][x] == 1:
                continue
            # 들여쓰기 올바르게 복원됨
            for dir in range(4):
                result = simulate(y, x, dir, field, d)
                max_result = max(max_result, result)

    print(f"#{tc} {max_result}")


