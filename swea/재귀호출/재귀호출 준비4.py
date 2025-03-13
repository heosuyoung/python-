def recur(x):
    if x==3:
        return
    for i in range(2):
        recur(x+1)
    print(x)
recur(0)