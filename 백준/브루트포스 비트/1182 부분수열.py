n,s=map(int,input().split())
arr=list(map(int,input().split()))
result=[]
cnt=0
def recursion(x):
    global cnt
    if sum(result)==s and len(result)>0:
        cnt+=1

    for i in range(x,n):
        result.append(arr[i])
        recursion(i+1)
        result.pop()
recursion(0)
print(cnt)