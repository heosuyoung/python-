from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
time=[0]*(n+1)
end_time=[0]*(n+1)

for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    for prev in data[1:]:
        if prev == -1:
            break
        else:
            graph[prev].append(i)
            indegree[i]+=1
q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
        end_time[i]=time[i]
while q:
    now=q.popleft()
    for next in graph[now]:
        indegree[next]-=1
        end_time[next]=max(end_time[next],end_time[now]+time[next])
        if indegree[next]==0:
            q.append(next)
for i in range(1,n+1):
    print(end_time[i])