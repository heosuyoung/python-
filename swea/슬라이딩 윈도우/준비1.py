arr=[4,5,1,1,5,4,-3,-13,9,20,13]
def get_sum(n):
    sum=0
    for i in range(n,n+5):
        sum+=arr[i]
    return sum
n=int(input())
print(get_sum(n))