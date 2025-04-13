'''
절단기 높이(h)를 지정하면 줄지어진 떡 한 번에 절단
ex) 높이 19,14,10,17인 떡이 있고 높이 15로 지정하면
  높이는  15,14,10,15 될거고 잘린 길이는 4,0,0,2
  손님이 왔을때 요청한 총길이가 M일때
  적어도 M만큼의 떡을 얻기위해 절단기에 설정한 높이의 최댓값 구하는 프로그램

#입력 예시
4 6 떡의 개수와 요청한 떡의 길이
19 15 10 7
'''
def binary_search(arr,m,start,end):
    result = 0
    while start<=end:
        mid=(start+end)//2
        total=0
        for x in arr:
            if x>mid:
                total += x-mid
        if total>=m:
            result=mid
            start=mid+1
        else:
            end=mid-1
    return result

n,m=map(int,input().split())
arr=list(map(int,input().split()))
print(binary_search(arr,m,0,max(arr)))
