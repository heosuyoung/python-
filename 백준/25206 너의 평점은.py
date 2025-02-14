grades=['A+','A0','B+','B0','C+','C0','D+','D0','F']
scores=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
total=0
result=0
for _ in range(20):
    subject,score,grade=input().split()
    score=float(score)
    if grade!='P':
       total += score
       result += score*scores[grades.index(grade)]
print('%.6f' %(result/total))

#풀이를 봤다 어떻게 해야할지 감이 안잡혀서
#학점과 등급을 따로 만들고
#횟수를 반복돌려버리고 P는 생략해야하니
#P가 아니라면 다 더한 후 인덱스를 활용해 곱한후
#나누어준다