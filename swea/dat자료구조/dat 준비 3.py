A=[5,2,5,7,3]
# n=int(input())
# def get_count():
#     cnt = 0
#     for i in range(len(A)):
#         if n in A[:]:
#             A.remove(n)
#             cnt+=1
#     print(cnt)
# get_count()

def get_count(n):
    cnt=0
    for i in range(len(A)):
        if A[i]==n:
            cnt+=1
    return cnt

n=int(input())
print(get_count(n))