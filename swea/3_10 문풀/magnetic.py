t=10
for _ in range(1,t+1):
    n=int(input())
    arr=[]
    cnt=0
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            if arr[j][i] ==1:
                for k in range(j + 1, n):
                    if arr[k][i] == 1:
                        break
                    elif arr[k][i] == 2:
                        cnt += 1
                        arr[j][i] = 0
                        arr[k][i] = 0
                        break
                    else:
                        continue
    print(f'#{_} {cnt}')




