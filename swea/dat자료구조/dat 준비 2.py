# A=[5,7,5,4,2,9]
# B=[5,4,2,5,6]
# def is_exist():
#     for i in range(len(A)):
#         if A[i] in B[:]:
#             print('O',end=" ")
#         else:
#             print('X',end=" ")
# is_exist()

A=[5,7,5,4,2,9]
B=[5,4,2,5,6]
def is_exist(n):
    for i in range(len(B)):
        if B[i] ==n:
            return 1
    return 0
for i in range(len(A)):
    if is_exist(A[i]):
        print('O',end=' ')
    else:
        print('X',end=' ')