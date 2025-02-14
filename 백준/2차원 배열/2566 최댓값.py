arr=[]
max_val=0
for _ in range(9):
    a=list(map(int,input().split()))
    arr.append(a)
#print(arr[1][0])
for i in range(9):
    for j in range(9):
        if arr[i][j]>max_val:
            max_val=arr[i][j]
print(max_val)
