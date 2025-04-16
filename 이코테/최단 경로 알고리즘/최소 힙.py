'''
import heapq
#오름차순 힙 정렬(heap sort)
def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,value) #h에 value를 넣음 heappush를 써서 heapq에 넣으면
    for i in range(len(h)):     #최솟값이 항상 앞에 오도록 트리형태유지
        result.append(heapq.heappop(h))#heappop은 항상 '최솟값'부터 꺼냄
    return result
result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
'''
#내림차순 힙 정렬(heap sort)
import heapq
def heapsort(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# h=[]
# heapq.heappush(h,3)
# heapq.heappush(h,5)
# heapq.heappush(h,4)
# heapq.heappush(h,2)
# heapq.heappush(h,1)
# print(h)


import heapq

graph = {
    1: [(2, 2), (3, 5)],
    2: [(3, 1), (4, 2)],
    3: [(4, 3)],
    4: []
}
INF=int(1e9)
distance = [INF]*5
distance[1]=0

heap=[]
heapq.heappush(heap,(0,1))

while heap:
    cost, now = heapq.heappop(heap)
    if distance[now]<cost:
        continue
    for neighbor,weight in graph[now]:
        new_cost = cost+weight
        if new_cost<distance[neighbor]:
            distance[neighbor] = new_cost
            heapq.heappush(heap,(new_cost,neighbor))