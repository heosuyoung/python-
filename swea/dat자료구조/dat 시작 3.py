text='BBQBHCBTS'
dat=[0]*200
for i in range(len(text)):
    dat[ord(text[i])] +=1
print(max(dat))