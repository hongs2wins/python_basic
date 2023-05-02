# Ch06 > sec2 > ploymorph.py
# 다형성(polymorph) : 공통 특성을 갖는 기본(super) 클래스로 부터 다양한 기능이 이루어질 수 있도록 하는 것

class Animal:
    name = None

    def __init__(self, name):
        self.name=name

    def cry(self):
        print(self.name + "이 웁니다.")

class Bird(Animal):
    def cry(self):
        print(self.name + "가 짹짹 웁니다.")

class Dog(Animal):
    def cry(self):
        print(self.name + "개가 멍멍 짖습니다.")

class Cat(Animal):
    def cry(self):
        print(self.name + "고양이가 야옹야옹 웁니다.")