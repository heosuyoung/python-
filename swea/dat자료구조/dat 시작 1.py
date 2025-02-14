# arr=[[1,5,10,15],[15,15,20,30]]
# n=int(input())
# def check_n():
#     cnt=0
#     for i in range(2):
#         for j in range(4):
#             if arr[i][j] == n:
#                  cnt+=1
#     return cnt
#
#
# print(check_n())


# arr=[[1,5,10,15],[15,15,20,30]]
# n=int(input())
# idx=0
# dat=[0]*31
# for i in range(2):
#     for j in range(4):
#         idx=arr[i][j]
#         dat[idx]+=1
# print(dat[n])

arr=[[1,5,10,15],[15,15,20,30]]
n=int(input())
idx =0
dat=[0] * 31
for i in range(2):
    for j in range(4):
        idx=arr[i][j]
        dat[idx]+=1
print(dat[n])