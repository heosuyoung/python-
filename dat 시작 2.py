text='ABCDE'
a = list(input().split())
dat=[0]*200
for i in range(len(text)):
    dat[ord(text[i])] += 1

for i in range(len(a)):
    if dat[ord(a[i])] >=1:
        print('O', end=' ')
    else:
        print('X',end=' ' )




# def check_word():
#     for i in range(len(a)):
#         if a[i] == text: return 1
#     return 0
# for i in range(len(a)):
#     if check_word():
#         print('O',end=' ')
#     else:
#         print('X',end=' ')


