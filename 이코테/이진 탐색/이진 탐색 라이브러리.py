'''
from bisect import bisect_left,bisect_right
a=[1,2,4,4,8]
x=4
print(bisect_left(a,x)) #4의 가장 왼쪽 인덱스 2와 4 사이인 인덱스 2
print(bisect_right(a,x)) #오른쪽인 인덱스 4
'''

#이걸 이용해서 값이 특정 범위에 속하는 데이터 개수 구할수있음
from bisect import bisect_left,bisect_right

def count_by_range(a,left_value,right_value):
    right_index=bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index-left_index
a=[1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))
#right index랑 left인덱스를 구해서 개수를 세면 범위 구함