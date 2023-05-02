# ch06 > sec1 > device.py
# 모듈명 : device, 클래스명 : Calculator, 맴버 필드(변수): a, b
# 멤버 함수(메소드) : add, avg, max, min
# 생성자 : __init

class Calculator:
    def __init__(self, a, *b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a + sum(self.b)
        return c

    def avg(self):
        c = (self.a + sum(self.b)) / (len(self.b)+1)
        return c

    def max(self):
        c = list(self.b)
        c.append(self.a)
        return max(c)
