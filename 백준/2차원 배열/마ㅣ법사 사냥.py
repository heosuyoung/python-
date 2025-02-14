N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
K=int(input())


def magic(y,x):
    dy=[-1,1,-1,1]
    dx=[1,1,-1,-1]
    sum_v=0
    for i in range(4): #방향 대각선 4방향
        for j in range(1,K+1): # 마법사의 파워
            ny=y+dy[i]*j #파워를 곱하는거임
            nx=x+dx[i]*j

            if ny<0 or nx<0 or ny>=N or nx>=N: continue
            sum_v += arr[ny][nx]

    return sum_v
result=0
for y in range(N):#행순회
    for x in range(N):
        result=max(result,magic(y,x))

print(result)
