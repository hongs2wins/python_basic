# ch02 > sec1 > ex2.py
# 변수(Variable) : 언제 값이 바뀔 수 있다.
# 기억장소(16진수 주소)의 이름 -> 변수명
# 파이썬의 변수 자료형은 데이터를 저장하므로써 정해진다.
# data1 변수에 3.14를 대입(저장) 하라
data1 = 3.14    # 실수(float) : 소숫점 이하 숫자가 있는 데이터
data2 = 1004    # 정수(int) : 소숫점 이하 숫자가 없는 데이터
data3 = "김기태"   # 문자열(str) : 여러 문자로 구성된 데이터
data4 = True    # 논리(bool) : True 아니면 False로 구성된 데이터
print("data1 : ", data1, type(data1), id(data1))
print("data2 : ", data2, type(data2), id(data2))
print("data3 : ", data3, type(data3), id(data3))
print("data4 : ", data4, type(data4), id(data4))