# ch03 > sec1 > ex22.py

name= "홍원준"
kor = 95
eng = 70
mat = 100
avg = (kor+eng+mat)/3
# Pan은 avg(세 과목 평균)이 70점 이상이고, 모든 과목의 점수가 60점 이상이면 "합격"
# 아니면 "불합격"으로 계산할 것
pan = ""
if avg >= 70 and kor >=60 and eng >=60 and mat >=60:
    pan = "합격"
else:
    pan = "불합격"

# 기타(etc)는 어느 한 과목이라도 100점 이 있으면, "과목우수" 이고,
# 아니면, ""으로 처리될 수 있도록 할 것.
etc = ""
if kor==100 or eng==100 or mat==100:
    etc="과목우수자"

# hak 은 avg(세 과목의 평균)이
# 97~99 100 A+, 93~96 A0, 90~92 A-
# 87~89 B+, 83~86 B0, 80~82 B-
# 77~79 C+, 73~76 C0, 70~72 C-
# 67~69 D+, 63~66 D0, 60~63 D-
# 60 미만 F 로 계산될 수 있도록 하되 중첩 if문을 활용할 것

hak =""
if avg >=90:
    hak="A"
elif avg >=80:
    hak="B"
elif avg >=70:
    hak="C"
elif avg>=60:
    hak="D"
else:
    hak="F"

if avg<60:
    hak=hak
elif avg%10>=7 or avg==100:
    hak=hak+"+"
elif avg%10>=3:
    hak=hak+"0"
# else:
#    hak=hak+"-"
elif avg%10>=0:
    hak=hak+"-"

print("이름 :", name, ",평균 :", avg, ", 판정 :", pan, ", 학정 :", hak)
print("기타 :",etc)