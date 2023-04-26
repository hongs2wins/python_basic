# 설문조사의 결과값을 매개변수로 받아 해당 값을 그래프로 출력하는 모듈 만들기
import matplotlib.pyplot as plt

def sur(lst):
    hit = [lst.count(1), lst.count(2), lst.count(3)]
    return hit

def prt(hot, label):
    # plt.rcParams["font.family"] = 'Nanum'
    # plt.rcParams["font.size"] = 20
    plt.pie(hot, labels=label, autopct='%.2f%%')
    plt.show()