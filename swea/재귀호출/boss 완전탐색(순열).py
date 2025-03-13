n=int(input())
path=[]
cnt=0
def count_dice():
    global cnt
    sum=0
    for i in range(n):
        sum+=path[i]
    if sum<=10:
        cnt+=1
    return cnt

def dice(x):
    if x==n:
        count_dice()
        return
    for i in range(1,7):
      path.append(i)
      dice(x+1)
      path.pop()
dice(0)
print(cnt)
'''
path = []
cnt = 0
n = int(input())

def kfc(lev, sum_v):
    global cnt
    if sum_v > 10:
        return

if lev == n:
    cnt += 1
    return

for i in range(1, 7):
    path.append(i)
    kfc(lev+1, sum_v + i)
    path.pop()
kfc(0,0)
print(cnt)
'''