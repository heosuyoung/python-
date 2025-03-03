import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

while True:
    w,h=map(int,input().split())

    if w==0 and h==0:
        break
    graph=[]
    result=[]
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    count=0
    dx=[-1,1,0,0,1,-1,-1,1]
    dy=[0,0,-1,1,1,-1,1,-1]

    def dfs(x,y):
        global count

        if x<0 or x>=h or y<0 or y>=w:
            return
        if graph[x][y]==1:
            count+=1
            graph[x][y]=0
            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs(nx,ny)
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                dfs(i,j)
                result.append(count)

    print(len(result))
