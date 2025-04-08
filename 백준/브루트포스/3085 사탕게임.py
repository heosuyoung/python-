n=int(input())
arr=[list(input()) for _ in range(n)]
result = 1


#개수세고
def count_candy():
    global result
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if arr[i][j]==arr[i][j-1]:
                cnt+=1
                #아니면 cnt를 1로 초기화해야함
            else:
                cnt=1
            result=max(result,cnt)
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if arr[j][i]==arr[j-1][i]:
                cnt+=1
            else:
                cnt = 1
            result = max(result, cnt)
    return result

#만약 옆이 다르면 좌우 바꿔야함
for i in range(n):
    for j in range(1,n):
        if  arr[i][j] != arr[i][j-1]:
            arr[i][j],arr[i][j-1]=arr[i][j-1],arr[i][j]
            result=max(result,count_candy())
            arr[i][j],arr[i][j-1]=arr[i][j-1],arr[i][j]
            # check하고 원상복귀 해줘야함

        if arr[j][i] != arr[j-1][i]:
            arr[j][i],arr[j-1][i]=arr[j-1][i],arr[j][i]
            result = max(result, count_candy())
            arr[j][i],arr[j-1][i]=arr[j-1][i],arr[j][i]

print(result)



