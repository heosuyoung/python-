arr=['A','B','C','D','E']
path=[]
def recur(cnt,start):
    if cnt==3:
        print(path)
        return
    for i in range(start,len(arr)):
        path.append(arr[i])
        recur(cnt+1,i+1)
        path.pop()

recur(0,0)