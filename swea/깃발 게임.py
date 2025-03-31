'''
테스트 케이스 받고
테케 만큼 반복
여는 시간o, 닫는시간e 받고
신청팀수 n 받고
신청팀 수 만 큼 반복
ex 10 11 11 14 15 16하면 끝이네

n번 반복하는데 n보다 크거나 같으면 추가해
그리고 그 거를 정렬해


'''
t=int(input())
for _ in range(1,t+1):
    o,e=map(int,input().split())
    n=int(input())
    arr=[]
    cnt=1
    for i in range(n):
        n,m=map(int,input().split())
        if n>=o and m<=e:
            arr.append([n,m])
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i][1]<=arr[i+1][0]:
            cnt+=1
        else:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    print(f'#{_} {cnt}')



