t=int(input())
for _ in range(t):
    cnt=0
    n=int(input())
    result=[]
    def recursion():
        global cnt
        if sum(result)==n:
            cnt+=1
            return

        if sum(result)>n:
            return

        for i in range(1,4):
            result.append(i)
            recursion()
            result.pop()
    recursion()
    print(cnt)