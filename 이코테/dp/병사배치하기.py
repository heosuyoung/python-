'''
첫쨰줄에 n
둘쨰줄에 각 병사의 전투력이 차례대로 주어지는데
해당 병사들이 내림차순으로 배열되게 만드는데 최대한 적게 열외시키는 수를 구하라
ex)
7
15 11 4 8 5 2 4면
4랑 2를 빼면 내림차순이 만들어짐 ->2

가장 긴 증가하는 부분 수열(lis알고리즘) 활용
모든 0<=j<i에 대하여, D[i] = max(D[i],D[j]+1) if arr[j]<arr[i]
'''
n=int(input())
arr=list(map(int,input().split()))
arr.reverse()
dp=[1]*n #가장 짧아도 1이므로

for i in range(1,n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)
#열외해야하는 병사 최소 수
print(n-max(dp))