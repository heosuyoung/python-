#주사위 3개를 던져 나올 수 있는 모든 조합을 출력
#종료조건: 주사위 3개를 던졌을떄 (level)
#branch 1~6
#

n=3
path=[]

def recur (cnt,start):
    if cnt==n:
        print(path)
        return

    for i in range(start,7):
        path.append(i)
        recur(cnt+1,i)
        path.pop()
recur(0,1)
