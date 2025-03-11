#내 코드
arr=[
    [0,1,1,1,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
visited=[0]*6
node=['A','B','T','Q','V','X']
def dfs(v):
    visited[v]=1
    print(v,end=' ')
    for i in range(len(arr)):
        if arr[v][i]==1 and visited[i]==0:
            dfs(i)
dfs(0)
# #강사님 코드
# MAP = [[0] * 6 for _ in range(6)]
# MAP[0][1] = 1
# MAP[0][2] = 1
# MAP[0][3] = 1
# MAP[1][4] = 1
# MAP[1][5] = 1
#
# def dfs(now):
#     print(now, end = ' ')
#     for i in range(6):
#         if MAP[now][i] == 0: continue
#         dfs(i)
#
# dfs(0)