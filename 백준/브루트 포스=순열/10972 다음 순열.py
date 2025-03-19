import sys
sys.setrecursionlimit(10**6)

n=int(input())
arr=list(map(int,input().split()))
result=[]
total=[]
visited=[0]*(n+1)
def dfs():
    if len(result)==n:
        #for i in range(len(result)):
        total.append(result[:])
        return

    for i in range(1,n+1):
        if visited[i] != 1:
            result.append(i)
            visited[i]=1
            dfs()
            result.pop()
            visited[i]=0
dfs()
#print(total)
found = False
for i in range(len(total)):
    if arr==total[i]:
        found = True
        if i == len(total)-1:
            print(-1)
        else:
            print(*total[i+1])
        break

if not found:
    print(-1)
