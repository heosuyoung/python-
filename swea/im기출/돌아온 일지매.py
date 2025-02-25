T=int(input())
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for _ in range(1,T+1):
    n=int(input())
    arr=[list(input()) for _ in range(10)]
    count = 0
    red = []
    green = []
    blue = []

    for i in range(10):
        for j in range(10):
            if arr[i][j]=='1':
                red.append((i,j))
            elif arr[i][j]=='2':
                green.append((i,j))
            elif arr[i][j]=='3':
                blue.append((i,j))
    for i,j in red:
        for k in range(4):
            for l in range(1,2):
                nx=i+dx[k]*l
                ny=j+dy[k]*l
                if 0<=nx<10 and 0<=ny<10:
                    if arr[nx][ny] in{'1','2','3','4'}:
                        break
                    else:
                        arr[nx][ny]='*'
    for i,j in green:
        for k in range(4):
            for l in range(1,3):
                nx=i+dx[k]*l
                ny=j+dy[k]*l
                if 0<=nx<10 and 0<=ny<10:
                    if arr[nx][ny] in{'1','2','3','4'}:
                        break
                    else:
                        arr[nx][ny]='*'
    for i,j in blue:
        for k in range(4):
            for l in range(1,4):
                nx=i+dx[k]*l
                ny=j+dy[k]*l
                if 0<=nx<10 and 0<=ny<10:
                    if arr[nx][ny] in{'1','2','3','4'}:
                        break
                    else:
                        arr[nx][ny]='*'

    for i in range(10):
        for j in range(10):
            if arr[i][j]=='0':
                count+=1
    print(f'#{_} {count}')