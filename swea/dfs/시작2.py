# arr=[
#     [1,3],
#     [2],
#     [0,3],
#     [2]
# ]
# visited=[0]*4
# def dfs(v):
#     visited[v]=1
#     print(v)
#     for i in range(len(arr)):
#         if visited[i]==0:
#             dfs(i)
# dfs(0)

arr=[
    [1,3],
    [2],
    [0,3],
    [2]
]
visited=[0]*4
def dfs(v):
    visited[v]=1
    print(v)
    for i in range(len(arr)):
        if visited[i]==0:
            dfs(i)
dfs(0)

#강사님 코드
# 인접 리스트
'''
m = [[] for _ in range(4)]
m[0] = [1, 3]
m[1] = [2]
m[2] = [0, 3]
m[3] = [2]
used = [0] * 4

# 시작 노드 방문 처리
used[0] = 1
def dfs(now):
    print(now)
    for i in range(len(m[now])):
        next = m[now][i]
        # used 검사(한번 갔던 곳은 안가겠다.)
        if used[next] == 1: continue
        # 방문했으면 방문했던 곳을 기록
        used[next] = 1
        # 재귀호출
        dfs(next)

dfs(0)

'''

# 인접행렬
'''
MAP = [[0] * 4 for _ in range(4)]

MAP[0][1] = 1
MAP[0][3] = 1
MAP[1][2] = 1
MAP[2][3] = 1
MAP[3][2] = 1
MAP[2][0] = 1

used = [0] * 4
used[0] = 1

def dfs(now):
    print(now)
    for i in range(4):
        if MAP[now][i] == 0: continue
        # 이미 갔던 곳이라면 무시
        if used[i] == 1: continue
        # 방문 표시
        used[i] = 1
        dfs(i)

dfs(0)
'''