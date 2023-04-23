# ch03 > sec1 > ex24.py
data = input("생년월일 입력[yyyymmdd]:")
day2 = int(data)     # 생년월일
year = data[0:4]    # 생년
month = int(data[4:6])  # 태어난 달
day = data[6:] # 태어난 일
birth = int(data[4:])   # 생일
birthstone = ""
if month==1:
    birthstone="가넷"
elif month==2:
    birthstone="자수정"
elif month==3:
    birthstone="아쿠아마린"
elif month==4:
    birthstone="다이아몬드"
elif month==5:
    birthstone="에메랄드"
elif month==6:
    birthstone="진주"
elif month==7:
    birthstone="루비"
elif month==8:
    birthstone="페리도트"
elif month==9:
    birthstone="사파이어"
elif month==10:
    birthstone="오팔"
elif month==11:
    birthstone="토파즈"
elif month==12:
    birthstone="터키석"

# 생년월일(yyyymmdd)을 입력받아
# 탄생월을 추출한 후 그 해당 월의 birthStone(탄생석)을 구하시오.
# 1월 : "가넷", 2월 : "자수정", 3월 : "아쿠아마린"
# 4월 : "다이아몬드", 5월 : "에메랄드", 6월 : "진주"
# 7월 : "루비", 8월 : "페리도트", 9월 : "사파이어"
# 10월 : "오팔", 11월 : "토파즈", 12월 : "터키석"

constellation = ""
# 년월일만 추출한 후 해당 날짜에 관한 constellation(별자리)를 구하시오.
# 12월 25일 ~ 01월 19일 : 염소자리 >=1225, <=119
# 01월 20일 ~ 02월 18일 : 물병자리 >=120, <=218
# 02월 19일 ~ 03월 20일 : 물고기자리 >=219, <=320
# 03월 21일 ~ 04월 19일 : 양자리  >=321, <=419
# 04월 20일 ~ 05월 20일 : 황소자리 >=420, <=520
# 05월 21일 ~ 06월 21일 : 쌍둥이자리
# 06월 22일 ~ 07월 22일 : 게자리
# 07월 23일 ~ 08월 22일 : 사자자리
# 08월 23일 ~ 09월 23일 : 처녀자리
# 09월 24일 ~ 10월 22일 : 천칭자리
# 10월 23일 ~ 11월 22일 : 전갈자리
# 11월 23일 ~ 12월 24일 : 사수자리

if birth>=1225 or birth<=119:
    constellation="염소자리"
elif birth>=120 and birth <=218:
    constellation="물병자리"
elif birth>=219 and birth <=320:
    constellation="물고기자리"
elif birth>=321 and birth <=419:
    constellation="양자리"
elif birth>=420 and birth <=520:
    constellation="황소자리"
elif birth>=521 and birth <=621:
    constellation="쌍둥이자리"
elif birth>=622 and birth <=722:
    constellation="게자리"
elif birth>=723 and birth <=822:
    constellation="사자자리"
elif birth >= 823 and birth <= 923:
    constellation = "처녀자리"
elif birth >= 924 and birth <= 1022:
    constellation = "천창자리"
elif birth >= 1023 and birth <= 1122:
    constellation = "전갈자리"
elif birth >= 1123 and birth <= 1224:
    constellation = "사수자리"

# 나이는  0230411를 기준으로 구함
today = 20230411
age = (today - day2) / 10000
print("당신의 나이는 ", int(age), "세 이며, 탄생석은 ", birthstone)
print("별자리는 ", constellation+"입니다.")
