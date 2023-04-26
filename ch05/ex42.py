# ch05 > sec1 > ex42.py
data1 = -20
data2 = 20
data3 = [1, True, 20, -15.34]
data4 = 'K'
data5 = 3.14159272
data6 = '20 * 4 - 8'
data7 = [70, 100, 90, 85, 75, 95, 100]
# builtins 내장 함수 알아보기
print("-20의 절대값 :",abs(data1))
print("20의 절대값 :",abs(data2))
print("data3은 모든 데이터가 True이거나 데이터가 존재하는가 :",all(data3))
print("data3은 하나만이라도 True이거나 데이터가 존재하는가 :",any(data3))
print(data6, "=", eval(data6))
print(data4,"의 아스키 코드값 :", ord(data4))
print(data2,"의 3승 값 :", pow(data2, 3))
print(data7,"을 정렬하면 : ", sorted(data7))