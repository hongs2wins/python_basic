# ch02 > sec2 > ex8.py
# 논리연산자 : 두 개의입력이 모두 True 또는 False 이며
# 출력은 True 또는 False 임 -> and, or, not
num1=100
num2=200
num3=300
print(num1>num2 and num2>num3)
print(num1>num2 and num2<num3)
print(num1<num2 and num2>num3)
print(num1<num2 and num2<num3)
print(num1>num2 or num2>num3)
print(num1>num2 or num2<num3)
print(num1<num2 or num2>num3)
print(num1<num2 or num2<num3)
print(not(num1>num2))