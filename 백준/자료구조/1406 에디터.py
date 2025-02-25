import sys
input=sys.stdin.readline

st1=list(input().rstrip())
st2=[]

N=int(input())

for _ in range(N):
    command=list(input().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))




















# string=list(input())
# N=int(input())
# cursor=len(string)
# for _ in range(N):
#
#     command=input().split()
#     if command[0]=='L' and cursor>0:
#         cursor -=1
#
#     elif command[0]=='D' and cursor<len(string):
#         cursor +=1
#
#     elif command[0]=='B' and cursor>0:
#         string.pop(cursor-1)
#         cursor-=1
#
#     elif command[0]=='P':
#         string.insert(cursor,command[1])
#         cursor+=1
#
# for i in range(len(string)):
#     print(string[i],end='')
