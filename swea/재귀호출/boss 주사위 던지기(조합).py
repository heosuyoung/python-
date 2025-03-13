n=int(input())
path=[]
def dice(cnt,start):
    if cnt==n:
        print(path)
        return
    for i in range(start,7):
        path.append(i)
        dice(cnt+1,i)
        path.pop()
dice(0,1)

