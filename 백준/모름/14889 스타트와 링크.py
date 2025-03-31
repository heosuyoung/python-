'''
n명이고 n은 짝수 n/2-> 스타트팀 n/2->링크 팀
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치
팀 능력치 -> 팀에 속한 모든 쌍의 능력치 Sij의 합
Sij와 Sji는 다를 수 있음 팀에 더해지는 능력치는 Sij와 Sji
두 팀의 능력치 차이를 최소로

모든 ex 4면
12,34
13,24
14,23 비교해서 최솟값

ex 8이면
1234,5678
1235
1236
1237
1238
1239
12

'''

'''
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
result=[]
price=float('inf')
def recursion(x):
    global price
    if len(result)==n//2:
        starteam=result[:]
        linkteam=[i for i in range(n) if i not in starteam]

        startability=0
        for i in starteam:
            for j in starteam:
                if i!=j:
                    startability+=arr[i][j]

        linkability = 0
        for i in linkteam:
            for j in linkteam:
                if i != j:
                    linkability += arr[i][j]

        diff=abs(startability-linkability)
        price=min(diff,price)

        return
    for i in range(x,n):
        result.append(i)
        recursion(i+1)
        result.pop()
recursion(0)
print(price)
'''

import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
result=float('inf')
visited=[0] * n
def dfs(x,cnt):
    global result
    if x==n//2:
        start=0
        link=0
        for i in range(n):
            for j in range(n):
                if visited[i]==1 and visited[j]==1:
                    start+=arr[i][j]
                elif visited[i]==0 and visited[j]==0:
                    link+=arr[i][j]
        diff=abs(start-link)
        result=min(diff,result)
        return
    for i in range(cnt,n):
        visited[i]=1
        dfs(x+1,i+1)
        visited[i]=0
dfs(0,0)
print(result)