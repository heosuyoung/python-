T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr= list(map(int,input().split()))

    max_v=arr[0]
    min_v=arr[0]

    for i in range(1,N):
        if min_v<arr[i]:
            min_v=arr[i]
        if max_v>arr[i]:
            max_v=arr[i]

    print(f'#{tc} {max_v-min_v}')