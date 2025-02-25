T = int(input())
for test_case in range(1, T + 1):
    N, M1, M2 = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)  # 역순으로 정렬

    # 첫 번째 탑과 두 번째 탑에 블록을 나눔
    tower_1 = []
    tower_2 = []
    for i in range(len(arr)):
        if len(tower_1) < M1 and len(tower_2) < M2:
            # 번갈아가며 넣음
            if len(tower_1) <= len(tower_2):
                tower_1.append(arr[i])
            else:
                tower_2.append(arr[i])
        elif len(tower_1) < M1:
            tower_1.append(arr[i])
        else:
            tower_2.append(arr[i])

    result = 0
    for i in range(len(tower_1)):
        result += tower_1[i] * (i + 1)  # 첫 번째 탑 1부터 시작
    for j in range(len(tower_2)):
        result += tower_2[j] * (j + 1)  # 두 번째 탑 1부터 시작

    print(f'#{test_case} {result}')