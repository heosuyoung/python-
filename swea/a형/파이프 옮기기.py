# dp(시간 짧음)
def solution():
    dp[0][1][0] = 1  # 첫 번째 파이프는 가로로 놓을 수 있음
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][i][0] = dp[0][i - 1][0]  # 첫 번째 행에서 가로 파이프 놓기(그냥 1로 하면 벽 만나는 경우의 처리가 안됨)

    for y in range(1, N):
        for x in range(1, N):

            # 대각선 파이프를 추가하는 과정
            if board[y][x] == 0 and board[y][x - 1] == 0 and board[y - 1][x] == 0:
                dp[y][x][2] = dp[y - 1][x - 1][0] + dp[y - 1][x - 1][1] + dp[y - 1][x - 1][2]

            # 가로 파이프를 추가하는 과정
            if board[y][x] == 0:
                dp[y][x][0] = dp[y][x - 1][0] + dp[y][x - 1][2]
                dp[y][x][1] = dp[y - 1][x][1] + dp[y - 1][x][2]


            # # 세로 파이프를 추가하는 과정
            # if board[y][x] == 0:

    # 최종 결과 출력
    sum_v = 0
    for i in range(3):  # 가로, 세로, 대각선 파이프의 모든 경우를 더해줌
        sum_v += dp[N - 1][N - 1][i]

    return sum_v

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    result = solution()
    print(f'#{tc} {result}')