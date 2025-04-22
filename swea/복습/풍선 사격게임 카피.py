t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    result=0
    def dfs(arr,total):
        global result
        if len(arr)==0:
            result=max(result,total)
            return

        for i in range(len(arr)):
            if len(arr)==1:
                cnt=arr[0]
            elif i==0:
                cnt=arr[1]
            elif i==len(arr)-1:
                cnt=arr[-2]
            else:
                cnt=arr[i-1]*arr[i+1]
            x=arr.pop(i)
            dfs(arr,total+cnt)
            arr.insert(i,x)

    dfs(arr,0)
    print(f'#{tc} {result}')


