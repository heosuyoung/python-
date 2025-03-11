#내 풀이
arr=[
    [0,1,1,1,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
node=['A','B','T','Q','V','X']
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==1:
print(arr[0][1])
# 강사님풀이
name = 'ABTQVX'

MAP = [[0] * 6 for _ in range(6)]
MAP[0][1] = 1
MAP[0][2] = 1
MAP[0][3] = 1
MAP[1][4] = 1
MAP[1][5] = 1

n = int(input())

for i in range(6):
    if MAP[n][i] == 0: continue
    print(name[i])