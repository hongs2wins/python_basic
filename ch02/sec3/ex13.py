# ch02 > sec3 > ex12.py
name= input("이름입력")
print("당신의 이름은 ?",name)
#
kor =int(input("국어점수 :"))
eng=int(input("수학점수 :"))
mat=int(input("영어점수 :"))
tot=kor+eng+mat
avg=tot/3
print("총점:",tot,"평균:",avg)
# 비만율 계산기
ht=float(input("신장 입력"))
tw=float(input("체중 입력"))
ps=ht/100
bi=tw/(ps*ps)
print("비만율:",bi)

print("010","123","4567")
print("010","123","4567",sep="-") #구분자

s1="홍원준"
a1=50
m1="male"
print("이름:",s1,end=", ")
print("나이:",a1,end=", ")  # 끝이 아니고 다음 출력도 이어서
print("성별:",m1)

# hlep
help(print)