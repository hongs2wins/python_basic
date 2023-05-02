# ch06 > sec1 > travel.py

class Flight:
    def __init__(self, name, price, amount):        # 기본 생성자 함수
        self.name = name
        self.price = price
        self.amount = amount

    def calc(self):                                 # 사용자 정의 함수1
        money = self.price * self.amount
        return money

    def prt(self):                                  # 내부 멤버를 호출하는 함수
        print(self.name,"요금총계 :%d" % self.calc())