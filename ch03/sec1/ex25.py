# ch03 > sec1 > ex25.py
wt = float(input("짐의 무게[kg] :"))    # 무게 입력
price = 0       # 요금
# 항공사에서 짐을 부칠 때 10kg 마다 10,000원 씩 수수료가 증가하며, 만약, 10kg 미만이면, 수수료는 없다.
if wt<10:
    price = 0
else:
    price = int(wt/10)*10000
print("요청하신 화물의 무게는 ", wt, "이며, 수수료는 ", price, "원 입니다.")
# 해당 메뉴에 대한 칼로리를 계산하여라
# 입력된 메뉴가 김밥이면 각 영양분은 지방(fat) : 18, 탄수화물(carboh) : 380, 단백질(protein) : 31
# 입력된 메뉴가 피자이면 각 영양분은 지방(fat) : 27, 탄수화물(carboh) : 430, 단백질(protein) : 17
# 입력된 메뉴가 떡볶이이면 각 영양분은 지방(fat) : 19, 탄수화물(carboh) : 395, 단백질(protein) : 7
# 입력된 메뉴가 치킨이면 각 영양분은 지방(fat) : 39, 탄수화물(carboh) : 138, 단백질(protein) : 98
# 입력된 메뉴가 기타이면 각 영양분은 지방(fat) : 25, 탄수화물(carboh) : 520, 단백질(protein) : 45

memu1 = int(input("메뉴[1.김밥 2.피자 3.떡볶이 4.치킨, 5.기타]"))
fat = 0
carboh = 0
protein = 0
name = ""

if memu1 == 1:
    fat=18
    cat=380
    protein=31
    name="김밥"
elif memu1 ==2:
    fat=27
    cat=430
    protein=17
    name="피자"
elif memu1 ==3:
    fat=19
    cat=395
    protein=7
    name="떡볶이"
elif memu1 ==4:
    fat=39
    cat=138
    protein=98
    name="치킨"
else:
    fat=25
    cat=520
    protein=45
    name="기타"

cal = fat * 9 + carboh * 4 + protein * 4

print("입력하신 메뉴는 ", name ,"이며, 총 칼로리는 ", cal, "입니다.")