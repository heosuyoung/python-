import sys
from collections import deque
input=sys.stdin.readline


def bfs(node):
    queue=deque([node])
    color[node]=1

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if color[i]==0:
                color[i]=color[v]*-1
                queue.append(i)
            else:
                if color[i]==color[v]:
                    return 'NO'
    return 'YES'


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)

    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, v + 1):
        if color[i] == 0:
            result = bfs(i)
            if result == 'NO':
                break
    print(result)
