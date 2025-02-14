def kfc(x):
    if x==3:
        return
    for _ in range(2):
        kfc(x+1)
    print(x)

kfc(0)