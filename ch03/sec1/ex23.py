# ch03 > sec1 > ex23.py
gender = int(input("성별[1.남 2.여]"))
ht = float(input("키[cm] :"))
wt = float(input("체중[kg] :"))
obesity = 0
# 비만율(obesity)은 성별이 남자인 경우 키에서 100을 빼고, 체중으로 나눈 값의 100을 곱한 값
# 성별이 여자인 경우 키에서 105를 빼고, 체중으로 나눈 값의 100을 곱한 값으로 계산한다.
if gender ==1:
    obesity=(ht-100)/wt*100
else:
    obesity=(ht-105)/wt*100
pan = ""
# 판정은 비만율이 125를 초과하면, "초고도비만", 115를 초과하면 "고도비만"
# 105를 초과하면 "비만", 95 이상이면, "정상", 85 이상이면, "체중미달",
# 85 미만이면 "초저체중"으로 한다.
if obesity > 125:
    pan = "초고도비만"
elif obesity >115:
    pan = "고도비만"
elif obesity >105:
    pan = "비만"
elif obesity >=95:
    pan = "정상"
elif obesity >=85:
    pan = "체중미달"
elif obesity <85:
    pan = "초저체중"
print("키 :", ht, ", 몸무게 :", wt)
print("비만율 :", obesity, ", 판정 :", pan)