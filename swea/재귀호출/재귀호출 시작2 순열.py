#순열은 방문배열사용
n=int(input())
path=[]
visited=[0]*(7)
def dice(x):
    if x==n:
        print(path)
        return

    for i in range(1,7):
        if visited[i]==1:
            continue
        visited[i]=1
        path.append(i)
        dice(x+1)
        path.pop()
        visited[i]=0
dice(0)