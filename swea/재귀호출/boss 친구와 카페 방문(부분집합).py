arr=list(input().split())
cnt=0
def get_count(tar):
    cnt = 0
    for i in range(len(arr)):
        if tar & 0x1:
            cnt +=1
        tar >>=1
    return cnt
answer=0
for i in range(1 << len(arr)):
    if get_count(i)>=2:
        answer+=1
print(answer)
