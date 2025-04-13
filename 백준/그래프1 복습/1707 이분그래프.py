#인접한 노드가 항상 '다른 집합'에 있어야함

import sys
from collections import deque
input= sys.stdin.readline
def bfs(node):
    queue=deque([node]) #시작하는 node를 queue에 넣음
    color[node]=1 #시작 노드를 1로칠함 dat사용하는거임

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if color[i]==0:
                color[i]=color[v]*-1 #v랑 인접한 노드를 다른색으로 칠함
                queue.append(i)
            else:
                if color[i]==color[v]:#만약 인접 노드가 같은색이라면
                    return 'NO'
    return 'YES'


k= int(input())
for _ in range(k):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)] #인접리스트
    color=[0] * (v+1)  #모두 0으로 만들어서 하나는 1 반대는-1로
    for _ in range(e):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    for i in range(1,v+1):
        if color[i]==0: #아직 bfs안돌렸으면 돌려라
            result=bfs(i)
            if result == 'NO': #만약 이분그래프 아니면 break
                break
    print(result)




