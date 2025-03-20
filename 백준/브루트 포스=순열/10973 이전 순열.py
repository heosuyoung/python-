n=int(input())
arr=list(map(int,input().split()))

check=False

for i in range(n-1,0,-1):
    if arr[i-1]>arr[i]: #이전 순열이 있으면
        for j in range(n-1,0,-1):
            if arr[i-1]>arr[j]:
                arr[i-1],arr[j]=arr[j],arr[i-1]
                arr=arr[:i]+sorted(arr[i:],reverse=True)
                check=True
                break
        if check:
            break
if check:
    print(*arr)
else:
    print(-1)

