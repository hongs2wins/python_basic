# ch05 > sec1 > ex43.py
# 사용자 정의 함수
# 사용자 정의 함수 종류 : 매개변수나 반환값의 유무에 따라
# 함수 정의
'''
def 함수명([매개변수명,...]):
    실행문
    [return 값]
'''
# 함수 호출
'''
모든 함수는 호출해야지 실행됨
[반환받을변수 = ] 함수명([매개값])
'''
def fnc1():         # 매개변수X, 반환X
    print("함수가 실행됩니다.")

def fnc2(a, b):     # 매개변수O, 반환X
    print("%d+%d=%d" % (a,b,a+b))

def fnc3():         # 매개변수X, 반환O
    return 1004

def fnc4(a, b):     # 매개변수O, 반환O
    return a-b

fnc1()
fnc2(20, 92)
a = fnc3()
print(a)
b = fnc4(88, 32)
print(b)


