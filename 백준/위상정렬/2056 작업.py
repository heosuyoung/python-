from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
time=[0]*(n+1)
end_time=[0]*(n+1)

for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    indegree[i]=data[1]
    for prev in data[2:]:
        graph[prev].append(i)
q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
        end_time[i]=time[i]
while q:
    now=q.popleft()
    for next in graph[now]:
        indegree[next]-=1
        end_time[next] = max(end_time[next], end_time[now] + time[next])

        if indegree[next]==0:
            q.append(next)
print(max(end_time))

