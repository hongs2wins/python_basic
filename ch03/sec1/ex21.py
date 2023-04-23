# ch03 > sec1 > ex21.py
# 제어문 : 조건문과 반복문
# 조건문 : 단순if, if~else~, if~elif~else~

# 단순 if
d = int(input("입력[1.예, 2.아니오] :"))
if d==1:
    print("예를 선택하셨습니다.")

# if else
su = int(input("점수 입력[0-100] :"))
if su>=70:
    print("합격~!")
else:
    print("불합격~!")

su = int(input("점수입력[0-100] :"))
pan =""
if su>=70:
    pan="합격"
else:
    pan="불합격"
print("판정 :",pan)

# if elif else 다단계 if
hak = ""
if su>=90:
    hak="수"
elif su>=80:
    hak="우" # 90미만 ~ 80이상(80~89)
elif su>=70:
    hak="미" # 80미만 ~ 70이상(70~79)
elif su>=60:
    hak="양" # 70미만 ~ 60이상(60~69)
else:
    hak="가" # 60미만
print("학점 :",hak)
