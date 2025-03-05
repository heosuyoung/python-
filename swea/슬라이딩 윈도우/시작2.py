n,m=map(int,input().split())
arr=list(map(int,input().split()))
def sliding_window():
    result=[]
    max_sum=sum(arr[:m])
    result.append(max_sum)
    for i in range(m,n):
        max_sum+=arr[i]-arr[i-m]
        result.append(max_sum)
    return result
print(sliding_window().index(max(sliding_window())))
