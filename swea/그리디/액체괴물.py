n=int(input())
arr=list(map(int,input().split()))
slime=[]
sum=0
arr.sort()
for i in range(n):
    sum=arr[0]+arr[1]
    slime.append(sum)
    arr.sort(reverse=True)
    arr.pop()
    arr.pop()
    if len(arr) ==0:
        break
    arr.append(sum)
    arr. sort()
result=0
for i in range(len(slime)):
    result+=slime[i]
print(result)