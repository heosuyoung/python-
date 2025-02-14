arr=list(map(int,input().split()))
arr.sort()
sum=0
for i in range(len(arr)-1):
    sum+=arr[i]*(len(arr)-(i+1))
print(sum)