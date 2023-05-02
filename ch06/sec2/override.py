# ch06 > sec2 > override.py
# super() : 부모의 생성자 함수

# super() : 부모의 생성자 함수
# pass : 함수의 추상화(기능을 정의하지 않음)

class Emp:
    name = None
    py = 0

    def __init__(self, name):
        self.name = name

    def pay(self):  # 추상화(Abstract)
        pass


class Perman(Emp):
    def __init__(self, name):
        super().__init__(name)

    def pay(self, base, bonus, grade):
        self.py = base + bonus + grade
        print("%s 직원의 총 급여 : %d" % (self.name, self.py))


class Temp(Emp):
    def __init__(self, name):
        super().__init__(name)

    def pay(self, per, hou):
        self.py = per * hou
        print("%s 직원의 총 급여 : %d" % (self.name, self.py))