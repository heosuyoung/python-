'''
1 2 3 4,,, 1 2 4,,,,1 4  4 8+4+4+4

3 10 1 2 5 ,,, 3 10 2 5,, 3 10 5  10,5  10  20+50+10+10+10



n만큼 돌려서 그 중 양 옆의 곱이 가장 큰 거를 제거
cnt에 그 양 엽의 곱을 더해
이거를 배열이 빌때 까지 반복
맨왼쪽의 경우와 맨 오른쪽의 경우 양 옆의 수가 없음 -> 1*오른쪽수 or 그냥 오른쪽 수만 하는 식으로 비교
그런데 배열의 수가 2가 된다면 옆의 수가 큰놈을 제거하고
그 옆의수를 cnt에 더해
배열의수가 1이 된다면 해당 값을 더하고 제거 -> while문이 끝날거임
n=10까지임 -> 10*9*8*7*6*5*4*3*2*1->360만 *T(50) ->1억8천->2초면 가능

이렇게 하니 예외 발생

3 10 1 2 5 경우 이렇게하면 최댓값이 구현이 안됨
dfs?
1,234 1,2,34,123,4 132 1324

'''
t=int(input())
for _ in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    answer=0
    def dfs(arr,total):
        global answer
        if len(arr)==0:
            answer=max(answer,total)
            return
        for i in range(len(arr)):
            if len(arr)==1:
                cnt=arr[0]
            elif i==0:
                cnt=arr[1]
            elif i==len(arr)-1:
                cnt=arr[-2]
            else:
                cnt=arr[i-1]*arr[i+1]
            x=arr.pop(i)
            dfs(arr,total+cnt)
            arr.insert(i,x)

    dfs(arr,0)
    print(f'#{_} {answer}')

#while arr:
    #     cnt = float('-inf')
    #     for i in range(len(arr)):
    #         if len(arr) == 1:
    #             if cnt < arr[0]:
    #                 cnt = arr[0]
    #                 idx = i
    #         elif i==0:
    #             if cnt<arr[1]:
    #                 cnt=arr[1]
    #                 idx=i
    #         elif i==len(arr)-1:
    #             if cnt<arr[-2]:
    #                 cnt=arr[-2]
    #                 idx=i
    #
    #         else:
    #             if cnt<arr[i-1]*arr[i+1]:
    #                 cnt=arr[i-1]*arr[i+1]
    #                 idx=i
    #     arr.remove(arr[idx])
    #     answer+=cnt
