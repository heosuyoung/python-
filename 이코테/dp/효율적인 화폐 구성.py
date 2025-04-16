n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]
d=[10001]*(m+1)
d[0]=0

for i in range(n): #화폐단위
    for j in range(arr[i],m+1): #금액,해당 금액부터 m까지
        if d[j-arr[i]] != 10001: #현재 금액에서 화폐단위를 뺀거를 만들수있다면,(i-k)원을 만드는 방법이 존재한다면
            d[j]=min(d[j],d[j-arr[i]]+1)
if d[m]== 10001:
    print(-1)
else:
    print(d[m])