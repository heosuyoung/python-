text='B[45]AB[9994]'
a=text.find('[')
b=text.find(']')
num1=text[a+1:b]
c=text.find('[',a+1)
d=text.find(']',b+1)
num2=text[c+1:d]
print(int(num1)+int(num2))
