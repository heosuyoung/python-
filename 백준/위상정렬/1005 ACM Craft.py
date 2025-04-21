from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(1,t+1):
    n,k=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    time=[0]+list(map(int,input().split()))
    end_time=[0]*(n+1)
    indegree=[0]*(n+1)
    for i in range(k):
        x,y=map(int,input().split())
        graph[x].append(y)
        indegree[y]+=1
    w = int(input())
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
    print(end_time[w])