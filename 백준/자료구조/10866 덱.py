from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
deq=deque()
for _ in range(n):
    a= input().split()

    if a[0] == 'push_front':
        deq.appendleft(a[1])
    elif a[0] == 'push_back':
        deq.append(a[1])
    elif a[0] == 'pop_front':
        if len(deq)>0:
            print(deq.popleft())
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if len(deq)>0:
            print(deq.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(deq))
    elif a[0] == 'empty':
        if len(deq)>0:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if len(deq)>0:
            print(deq[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(deq)>0:
            print(deq[-1])
        else:
            print(-1)