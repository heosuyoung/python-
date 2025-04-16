'''
어떤 나라에는 n개의 도시가있다
그리고 각 도시는 보내고자 하는 메시지가 있는 경우 다른 도시로 전보를 보내서 메시지 전송
x도시에서 y도시로 전보를 보낼거면
x에서 y로 향하는 통로가 있어야함
ex) x->y있지만 y->x없으면 불가능
어느날 c도시에 위급 상황 발생
최대한 많은 도시로 메시지 보낼거임
메시지는 도시 c에서 출발해 도시에 설치된 통로 통해 최대한 많이 퍼져나가게!
도시의 번호와 통로가 설치 도있고
도시c에서 보낸 메시지를 받게 되는 도시 개수랑 도시들이 메시지 받는데 걸리는 시간
계산

#첫째줄에 도시개수 N, 통로개수M,메시지를 보내고자 하는도시 C
둘째줄 부터 M+1번째 줄에 통로 X,Y,Z가 주어짐
X,Y는 도시 메시지 ,전달되는 시간은 Z
C에서 보낸 메시지를 받는 도시 총개수와 걸리는 시간출력

ex
입력
3 2 1
1 2 4
1 3 2
출력
2 4
'''

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

n,m,start=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[INF] * (n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
dijkstra(start)

count = 0
max_distance=0
for d in distance:
    if d != 1e9:
        count+=1
        max_distance=max(max_distance,d)
print(count-1,max_distance)