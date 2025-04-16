'''
입력값
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
각 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력
왼쪽 위에서 오는 경우
왼쪽 아래에서 오는 경우
왼쪽에서 오는 경우
'''
for tc in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    dp=[]
    index=0
    #금광이 한줄에 다 들어오므로 m에 맞춰서 끊음
    for i in range(n):
        dp.append(arr[index:index+m])
        index+=m
    for j in range(1,m):
        for i in range(n):
            if i==0:
                left_up=0
            else:
                left_up=dp[i-1][j-1]
            if i==n-1:
                left_down=0
            else:
                left_down=dp[i+1][j-1]
            left=dp[i][j-1]
            dp[i][j]=dp[i][j]+max(left_up,left_down,left)
    result=0
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)
