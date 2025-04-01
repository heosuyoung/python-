
#순서대로 찾되 찾으면 0로 만들어 버리고 다음 숫자를 찾는 형식으로
#하면 될듯하다
#해당 배열을 튜플로 중복되는 거 없게 값을 배열에 넣음
#그러면 해당 배열 숫자를 구하는 식으로, 구하면 그 숫자를 해당 배열에서 빼고
#arr에서는 -1로 바꿈 그리고 해당 배열을 다 뺄때까지 반복
t=int(input())
for _ in range(1,t+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    dx=[1,0,0,-1]
    dy=[0,1,-1,0]
    apple=[]
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                apple.append(arr[i][j])
    apple=sorted(list(tuple(apple)))
    while apple:
        for i in range(4):
            for j in range(1,i+1):
                nx=x+dx*n


    #오른쪽으로 가다가 해당 ex [1][0]으로 가다가 [1][0]~[1][n]에 arr[0]가 있다면?
    #거기서 cnt+=1로 하고 [1][n]까지 쭉가고 apple.pop(0)해주고
    #해당 값은 -1로 바꿔주고 거기서 반복(while apple배열 빌떄까지)
    for i in range(n):






    print(f'#{_} {cnt}')

