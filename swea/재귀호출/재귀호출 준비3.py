# def count_re(x):
#     if x==6:
#         return
#     print(x,end=' ')
#     count_re(x+1)
#     print(x,end=' ')
# count_re(0)

def count_re(x):
    if x==6:
        return
    print(x,end=' ')
    count_re(x+1)
    print(x,end=' ')
count_re(0)