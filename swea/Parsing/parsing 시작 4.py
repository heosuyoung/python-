text='ABCDEFABCKKKKKABC'
cnt=0
a=0
b=0
while True:
    b=text.find('ABC',a)
    if b== -1:
        break
    cnt+=1
    a=b+1
print(cnt)