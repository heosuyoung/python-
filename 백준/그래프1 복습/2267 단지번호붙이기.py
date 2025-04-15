# from collections import deque
# import sys
#
# input=sys.stdin.readline
# n=int(input())
# maps=[list(map(int,input().strip())) for _ in range(n)]
# result=[]
# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
# def bfs(maps,a,b):
#     queue=deque()
#     queue.append([a,b])
#     maps[a][b]=0
#     cnt=1
#     while queue:
#         x,y,=queue.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=n:
#                 continue
#             if maps[nx][ny]==1:
#                 maps[nx][ny]=0
#                 queue.append([nx,ny])
#                 cnt+=1
#     return cnt
#
#
# for i in range(n):
#     for j in range(n):
#         if maps[i][j]==1:
#             count=bfs(maps,i,j)
#             result.append(count)
# result.sort()
# print(len(result))
# for i in result:
#     print(i)


from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
maps=[list(map(int,input().strip())) for _ in range(n)]
result=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(maps,a,b):
    cnt=1
    queue=deque()
    queue.append([a,b])
    maps[a][b]=0
    while queue:
        x,y=queue.popleft()
        maps[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=0
                queue.append([nx,ny])
                cnt+=1
    return cnt


for i in range(n):
    for j in range(n):
        if maps[i][j]==1:
            cnt=bfs(maps,i,j)
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)























