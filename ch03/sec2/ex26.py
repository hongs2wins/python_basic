# ch03 > sec2 >ex26.py
# 반복실행문 : while, do~while, for

'''
while문 : 해당 조건식이 만족할 동안만 실행
카운트변수=0
while 조건식:
    카운트변수증감식
    반복실행문장
'''

ax = 0  # 카운트변수
while ax<10:
    ax = ax + 1   # 증감식
    print("나무를 %d번 찍습니다."% ax)  #반복실행문장
print("열번찍어 안 넘어가는 나무 없네")

ax = 0  # 카운트변수
while ax>-10:
    ax = ax - 1   # 증감식
    print("나무를 %d번 찍습니다."% ax)  #반복실행문장

# 1~10합산 결과 계산하여 출력
n=0
tot=0
while n<10:
    n+=1   # n=n+1
    tot=tot+n
#    print(n, "번째, tot=",tot)
print("합산결과",tot)

# 2~100 의 짝수의 합을 계산하여 출력
n=0
tot=0
while n<100:
    n = n + 2
    tot=tot + n
print ("합산결과",tot)

# 2~100 의 짝수의 합을 계산하여 출력 (별식)
n=0
tot=0
while n<100:
    n+=1
    if n % 2 == 0:
        tot = tot + n
print("합산결과",tot)

# 1~100 의 홀수 의 합을 계산
n=1
tot=0
while n<100:
    tot=tot+n
    n=n+2
print("홀수 합산결과",tot)

# 1~100 의 홀수 의 합을 계산 (별식1)
n=0
tot=0
while n<100:
    n=n+1
    if n % 2 ==1:
        tot=tot+n
print("홀수 합산결과",tot)

# 1~100 의 홀수 의 합을 계산 (별식2)