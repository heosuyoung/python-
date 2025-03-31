n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[0]*n
result=float('inf')

def dfs(x):
    if start+link==n:
        return

    for i in range(n):
