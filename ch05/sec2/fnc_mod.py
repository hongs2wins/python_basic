# ch05 > sec2 > fnc_mod
# 피타고라스 함수와 모테카를로 함수 만들기
# 피타고라스 정리
# 삼각형에서 가장 긴 변의 길이의 제곱은 다른 두 변의 제곱을 더한 값과 같다.
# 빗변의 길이를 구하는 함수(pytha)를 정의하시오.

import math
def pytha(s, t):        # S: 밑변의 너비, t:높이의 크기, l:빗변의 길이
    l=math.pow(s,2)+math.pow(t,2)   # l=s**2 + t**2
    return math.sqrt(l)             #return l**(1/2)

# print(pytha(3,4))

# 몬테카를로 시뮬레이션
# 실제로 시험이 힘들 경우 가상으로 실제 모의시험을 할 수 있는 시뮬레이션 모델
# n번의 임의 값 발생 모델

from random import randint
def coin(n):
    lst=[]
    for i in range(0,n):
        lst.append(randint(0,1))
    return lst

# 임의 발생된 데이터의 확률 계산
def monte(n):
    ls=coin(n)
    print("앞면이 나올확률 : %5.2f" % (ls.count(0)/n))
    print("뒷면이 나올확률 : 5.2%f" % (ls.count(1)/n))