import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

def recursion(i):
    if i>=n:
        return 0

    #현재 날짜를 선택
    result=0
    if i + arr[i][0]<=n:
        result=arr[i][1]+recursion(i+arr[i][0])
    #현재 날짜 생략
    skip=recursion(i+1)

    return max(result,skip)

print(recursion(0))