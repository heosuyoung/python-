def solve():
    size=len(arr)
    cnt=0
    for i in range(size):
        for tar in range(i):
            i_a,i_b=arr[i][0],arr[i][1]
            tar_a,tar_b=arr[tar][0],arr[tar][1]
            if i_b<tar_b:
                cnt+=1
    return cnt

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[]
    for i in range(n):
        x,y=map(int,input().split())
        arr.append((x,y))
    arr.sort(key=lambda x:x[0])
    # for i in range(n-1):
    #     if arr[i+1][0]>arr[i][0] and arr[i+1][1] < arr[i][1]:
    #        cnt+=1
    # for i in range(n-1):
    #     if arr[i+1][0]<arr[i][0] and arr[i+1][1] > arr[i][1]:
    #        cnt+=1
    result=solve()
    print(f'#{tc} {result}')