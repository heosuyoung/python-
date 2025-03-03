# #dfs
# import sys
# from collections import deque
# input=sys.stdin.readline
#
# N=int(input())
#
# graph=[] #입력받을 그래프
# result=[] #결과 출력할 리스트
# count=0
#
# for _ in range(N):  #그래프에 숫자 담기
#     graph.append(list(map(int,input().rstrip())))
#
# dx=[-1,1,0,0] #4방향 순회
# dy=[0,0,-1,1]
#
# def dfs(x,y):
#     global count
#
#     if x<0 or x>=N or y<0 or y>=N:
#         return #범위 넘어가면 return
#     if graph[x][y]==1:
#         count+=1 #그래프가 1이면 count1올리고
#         graph[x][y]=0 #해당 그래프 0으로 만듬
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             dfs(nx,ny) #1발견할수 없을떄 까지 재귀반복
# #원소가 1일때만 dfs로 집 방문
# for i in range(N):
#     for j in range(N):
#         if graph[i][j]==1:  #그래프가 1일때 dfs돌리는거임
#             dfs(i,j)
#             result.append(count) #result에 count 추가하고
#             count=0 #count초기화
# result.sort() #오른차 순 정렬하고
#
# print(len(result))
# for k in result:
#     print(k) #결과 출력
#
#bfs

import sys
from collections import deque
from itertools import count

input=sys.stdin.readline
N=int(input())
graph=[]
result=[]

for _ in range(N):
    graph.append(list(map(int,input().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph,a,b):
    queue=deque()
    queue.append([a,b])
    graph[a][b]=0 #첫번쨰 집 방문처리
    count=1 #첫번쨰 집부터 시작해서

    while queue:
        x,y=queue.popleft()
        graph[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>= len(graph) or ny<0 or ny>=len(graph):
                continue

            if graph[nx][ny]==1: #1이라면(방문을 안했다면)
                graph[nx][ny]=0 #방문하고(0으로만들고)
                queue.append([nx,ny]) #거기서 queue에 추가 한후 또 반복
                count+=1
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            count=bfs(graph,i,j)
            result.append(count)
result.sort()
print(len(result))
for k in result:
    print(k)