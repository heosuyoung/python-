# n=int(input())
# arr=[list(map(int,input().split())) for _ in range(n)]
# result=[]
# total=float('inf')
# # 1->2->3->4  ->1
# # 1->2->4->3  ->1
# # 1->3->2->4   ->1
# # 1->3->4->2   ->1    방문 표시해서 모든 순열 돌리고 ->돌아오는 값
# visited=[0]*n
# def dfs(current,cost):
#     global total
#     if len(result)==n:
#         #만약 돌아오지 못한다면
#         if arr[current][result[0]] == 0:
#             return
#         #현재 값에다가 돌아오는 값을 더해서
#         total=min(total,cost + arr[current][result[0]])
#         return
#     for next in range(n):
#         if visited[next]!=1 and arr[current][next] !=0:
#                 result.append(next)
#                 visited[next]=1
#                 dfs(next,cost+arr[current][next])
#                 result.pop()
#                 visited[next]=0
# visited[0]=1
# result.append(0)
# dfs(0,0)
# print(total)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
total = float('inf')
visited = [False] * n

def dfs(current, cost):
    global total
    # 모든 도시를 방문했다면 (visited 배열의 True 개수가 n이면)
    if sum(visited) == n:
        # 현재 도시에서 시작 도시(0번)로 돌아갈 수 있는지 확인
        if arr[current][0] == 0:
            return
        total = min(total, cost + arr[current][0])
        return
    for i in range(n):
        if not visited[i] and arr[current][i] != 0:
            visited[i] = True
            dfs(i, cost + arr[current][i])
            visited[i] = False

# 시작 도시는 0번으로 고정
visited[0] = True
dfs(0, 0)
print(total)
