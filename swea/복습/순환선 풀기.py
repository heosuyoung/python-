
def dfs(x):
    global result,price
    if len(result)==4:
        a,b,c,d=result
        total1=(arr[a]+arr[d])**2+(arr[1]+arr[2])**2
        total2=(arr[0]+arr[1])**2+(arr[2]+arr[3])**2
        price=max(price,total1,total2)
        return

    for i in range(x,n):
        if (i==0 and n-1 in dat) or (i==n-1 and 0 in dat):
            continue
        if all(abs(i-d) != 1 for d in dat):
            result.append(i)
            dat.append(i)
            dfs(i+1)
            result.pop()
            dat.pop()


t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    price=float('-inf')
    result=[]
    dat=[]
    dfs(0)
    print(f'#{tc} {price}')
