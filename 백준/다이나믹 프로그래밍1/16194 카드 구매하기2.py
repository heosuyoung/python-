n=int(input())
p=[10001]+list(map(int,input().split()))
dp=[0]+[10001]*(n)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=min(dp[i],dp[i-j]+p[j])
print(dp[n])
