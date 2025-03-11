arr=[
    [],
    [0,1,0,0,0],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0]
]
node='12345'
n=int(input())
for i in range(5):
    if arr[n][i]==0:
        continue
    print(node[i])