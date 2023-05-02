# ch06 > sec2 > inherit.py

# 부모 클래스(Super Class) : 상위 클래스로 조상이 되는 클래스를 말함
class Origin:           # 슈퍼 클래스 = 부모 클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("이름 : %s, 나이 : %d" % (self.name, self.age))

    def calc(self):
        print("%d년생 :" % (2023 - self.age + 1))


# 자식 클래스(Sub Class)
class Destroy(Origin):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("이름 : %s, 나이 : %d, 성별 : %s" % (self.name, self.age, self.gender))

# 오버라이딩(Override) : 부모 클래스로 부터 물려 받은 멤버의 형태를 변형하는 것