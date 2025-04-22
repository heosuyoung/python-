from copy import deepcopy
from collections import deque

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    time=[0]*(n+1)
    indegree=[0]*(n+1)
    graph=[ [] for _ in range(n+1)]

    for i in range(1,n+1):
        data=list(map(int,input().split()))
        time[i]=data[0]
        indegree[i]=data[1]
        for prev in data[2:]:
            graph[prev].append(i)
    min_total_time=float('inf')
    for coco in range(1,n+1):
        coco_time=time[:]
        coco_indegree=indegree[:]
        coco_graph=deepcopy(graph)

        coco_time[coco]//=2

        end_time=[0]*(n+1)
        q=deque()
        for i in range(1,n+1):
            if coco_indegree[i]==0:
                q.append(i)
                end_time[i]=coco_time[i]
        cnt=0
        while q:
            now=q.popleft()
            cnt+=1
            for next in graph[now]:
                coco_indegree[next]-=1
                end_time[next]=max(end_time[next],end_time[now]+coco_time[next])
                if coco_indegree[next]==0:
                    q.append(next)
        if cnt<n:
            continue
        min_total_time=min(min_total_time,max(end_time))
    print(f'#{tc} {min_total_time if min_total_time != float("inf") else -1} ')
        
