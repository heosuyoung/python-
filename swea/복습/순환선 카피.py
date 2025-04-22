t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    answer=float('-inf')
    result=[]
    dat=[]

    def dfs(x):
        if len(result)==4:
            global answer
            total1=(result[0]+result[3])**2+(result[1]+result[2])**2
            total2=(result[0]+result[1])**2+(result[2]+result[3])**2
            answer=max(answer,total1,total2)
            return

        for i in range(x,n):
            if (i==0 and n-1 in dat) or (i==n-1 and 0 in dat):
                continue
            if all(abs(i-d)!= 1 for d in dat):
                result.append(arr[i])
                dat.append(i)
                dfs(i+1)
                result.pop()
                dat.pop()
    dfs(0)
    print(f'#{tc} {answer}')