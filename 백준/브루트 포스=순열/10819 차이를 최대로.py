n=int(input())
arr=list(map(int,input().split()))
arr.sort()
result=[]
total=0
totals=0
def dfs():
    global totals
    global total
    if len(result)==n:
        for i in range(n-1):
            total += abs(result[i] - result[i + 1])
            totals=max(totals,total)
        return totals
    for i in range(n):
        result.append(arr[i])
        dfs()
        result.pop()

print(dfs())

