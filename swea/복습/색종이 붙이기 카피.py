def promise(a,a2,b,b2):
    for i in range(a,a2+1):
        for j in range(b,b2+1):
            if not paper[i][j]:
                return False
    return True

def attach(a1,a2,b1,b2,w):
    for i in range(a1,a2+1):
        for j in range(b1,b2+1):
            paper[i][j]=w

def glue(p):
    global result
    for y in range(10):
        for x in range(10):
            if paper[y][x]:
                for k in range(5):
                    ny,nx=y+k,x+k
                    if confetti[k] and ny<10 and nx<10:
                        if promise(y,ny,x,nx):
                            attach(y,ny,x,nx,0)
                            confetti[k]-=1
                            glue(p+1)
                            confetti[k]+=1
                            attach(y,ny,x,nx,1)
                return
    result=min(result,p)

t=int(input())
for tc in range(1,t+1):
    paper=[list(map(int,input().split())) for _ in range(10)]
    confetti=[5]*5
    result=26
    glue(0)
    print(f'#{tc} {result if result != 26 else -1}')