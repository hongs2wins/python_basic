# ch02 > sec1 > ex3.py
# 형변환(casting) : 현재 자료형에서 다른 자료형으로 변환하는 것
data1 = "1004" # str -> int
data2 = "3.14" # str -> float
data3 = "True" # str -> bool
data4 = "홍원준" # 문자는 형변환이 안된다.
data5 = "5*4/3"
# 모든 등호(대입) 연산은 오른쪽 부터 실행됨
data1 = int(data1)
data2 = float(data2)
data3 = bool(data3) # 만약 문자열의 데이터가 계산식이면, 계산함
print("data1 : ", data1, type(data1))
print("data2 : ", data2, type(data2))
print("data3 : ", data3, type(data3))
print("data4 : ", data4, type(data4))
print("data5 : ", data5, type(data5))

