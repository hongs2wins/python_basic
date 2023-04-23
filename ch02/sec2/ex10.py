# ch02 > sec2 > ex10.py
# 비트 연산자 : &,(and) |(or), ^(입력이 서로다를경우), ~(보수) 등의 2진수 연산
a=223
b=241
print("a=", bin(a))
print("b=",bin(b))
# print("&=", bin(a & b))
# print("|=", bin(a | b))
print("^=",bin(a^b))
print("~=", bin(~a))

a=bin(223)
b=bin(241)
print(a)
print(b)
# print("&=", bin(a & b))
# print("|=", bin(a | b))
print("^=",bin(a^b))
print("~=", bin(~a))
