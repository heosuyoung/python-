#중복순열은 그냥 방문배열 필요x
path=[]
def recur(x):
    if x==3:
        print(path)
        return
    for i in range(1,7):
        path.append(i)
        recur(x+1)
        path.pop()

recur(0)