# ch04 > sec3 > ex37.py
import random
su = random.random()     # 0~1 의 숫자 아무거나(랜덤수)
num = random.randint(1, 100)    # 1~100의 정수 아무거나(랜덤정수)
print(su)
print(num)

# 로또 추첨기 (1~45의 정수 중복없이 여섯 개 추출하여 출력)
res = []
while len(res) < 6:
    num = random.randint(1, 45)
    if num not in res:
        res.append(num)
print(sorted(res))

# 특정 횟수 만큼 로또645 번호 추출
h = int(input("게임하실 횟수 :"))
for i in range(0, h):
    res = []
    while len(res) < 6:
        num = random.randint(1, 45)
        if num not in res:
            res.append(num)
    print(sorted(res))
