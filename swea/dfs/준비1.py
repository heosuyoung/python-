arr=[
    [0,0,0,0],
    [1,0,0,0],
    [1,1,0,0],
    [1,1,0,0]
]
node='BTAR'
n=int(input())
for i in range(4):
    if arr[n][i]==1:
        print(node[i])