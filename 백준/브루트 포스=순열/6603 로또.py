while True:
    arr=list(map(int,input().split()))
    if arr[0]==0:
         break
    result=[]
    def dfs(x):
        if len(result)==arr[0]:
            print(*result)
            return


        for i in range(x,arr[0]+1):
            result.append(arr[i])
            dfs(i+1)
            result.pop()
    dfs(1)
    print()





