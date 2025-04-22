#import sys
from collections import deque
from itertools import combinations

#input = sys.stdin.readline
MAX = float('inf')

def bfs(area, graph, people):
    visited = set()
    q = deque([area[0]])
    visited.add(area[0])
    total = people[area[0]]

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt in area and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
                total += people[nxt]

    return total if len(visited) == len(area) else None


def solve(N, people, graph):
    result = MAX
    for r in range(1, N // 2 + 1):
        for comb in combinations(range(1, N+1), r):
            area1 = list(comb)
            area2 = [i for i in range(1, N+1) if i not in area1]
            sum1 = bfs(area1, graph, people)
            sum2 = bfs(area2, graph, people)
            if sum1 is not None and sum2 is not None:
                result = min(result, abs(sum1 - sum2))
    return -1 if result == MAX else result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        row = list(map(int, input().split()))
        for j in range(1, N + 1):
            if row[j - 1] == 1:
                graph[i].append(j)
    people = [0] + list(map(int, input().split()))
    res = solve(N, people, graph)
    print(f'#{tc} {res}')
