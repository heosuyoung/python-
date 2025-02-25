T = int(input())
for _ in range(1,T+1):
    N = int(input())
    lightening = list(map(int, input().split()))

    arr = [0]*(N+1)
    cnt = 0

    for i in range(1,N+1):
        if arr[i] != lightening[i-1]:
            cnt += 1
            for j in range(i,N+1,i):
                arr[j] = 1-arr[j]

    print(f'#{_} {cnt}')