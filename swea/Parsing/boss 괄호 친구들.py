word=input()
num=0
b=0
d=0
start1=word.find('[',b)
end1=word.find(']',b)

start2=word.find('{',d)
end2=word.find('}',d)

#print(word[start1+1:end1])
if word.find('[',b)< word.find('{',d):
    num += word[start1+1:end1]
    b+=start1+1
else:
    num*=word[start2+1:end2]
    d+=start2+1
print(num)
