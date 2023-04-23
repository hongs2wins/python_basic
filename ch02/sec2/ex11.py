# ch02 > sec2 > ex11.py
a = 200
b = 300
# 파이썬은 맞교환이 가능하다.
'''
imsi = a
a = b
b = imsi
'''
print("교환전")
print("a=", a)
print("b=", b)
a, b = b, a
print("교환후")
print("a=", a)
print("b=", b)

lst = [50, 70, 40, 60, 80]
a1, *a2 = lst
print("lst=", lst)
print("a1=", a1)
print("a2=", a2)
*b1, b2 = lst
print("b1=", b1)
print("b2=", b2)
