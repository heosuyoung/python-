block=100
n=int(input())
block_list=list(map(int,input().split()))
block_list.sort()
cnt=0

for i in range(len(block_list)):
    while block > 0:
        block -= block_list[i]
        if block>=0:
            cnt+=1
        break
print(cnt)