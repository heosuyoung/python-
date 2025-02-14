n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort()
cnt=1
start=arr[0][1]
for i in range(n):
    if arr[i][0]>start:
        cnt+=1
        start=arr[i][1]
    else:
        continue
print(cnt)