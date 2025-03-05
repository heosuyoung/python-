arr=[4,5,1,1,5,4,-3,-13,9,20,13]
def get_sum():
    a=len(arr)
    k=5
    result=[]
    max_sum=sum(arr[:k])
    result.append(max_sum)
    for i in range(k,a):
        max_sum+=arr[i]-arr[i-k]
        result.append(max_sum)
    return result
print(get_sum().index(max(get_sum())))