text=['GOLDABCGOLD','HELLOWROLD','WHITEGOLD']

num=0
def find_gold(tex):
    a=0
    cnt=0
    b=0
    while True:
        b=tex.find('GOLD',a)
        if b==-1:
            break
        cnt+=1
        a=b+1
    return cnt

for tex in text:
    num+=find_gold(tex)
print(num)
