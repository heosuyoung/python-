t=int(input())
for _ in range(1,t+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    result=[]
    price=float('inf')
    def dfs(x):
        global cnt
        global price
        if len(result)==n//2:
            a_te=result[:]
            b_te=[i for i in range(n) if i not in a_te]
            a_taste=0
            for i in a_te:
                for j in a_te:
                    if  i!=j:
                        a_taste+=arr[i][j]

            b_taste = 0
            for i in b_te:
                for j in b_te:
                    if i != j:
                        b_taste += arr[i][j]

            diff=abs(a_taste-b_taste)
            price=min(price,diff)
            return

        for i in range(x,n):
            result.append(i)
            dfs(i+1)
            result.pop()


    dfs(0)
    print(f'#{_} {price}')