# ch02 > sec3 > ex15.py
radius = int(input("반지름 입력:"))
pi = 3.14159
area = radius * radius * pi
length = radius * 2 * pi
price=int(length)*100
print("반지름 : ",format(radius, "3d"))
print("원주율 : ",format(pi, "8.3f"))
print("원의 넓이 : ",format(area, "9.4f"))
print("원의 길이 : ",format(length,"8.5f"))
print("가격 :",format(price, "3,d"))