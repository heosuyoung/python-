# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             for l in range(1,4):
#                 print(i,j,k,l)

path=[]
def recur(cnt):
    if cnt==4:
        print(*path)
        return

    for i in range(1,4):
      path.append(i)
      recur(cnt+1)
      path.pop()
recur(0)

