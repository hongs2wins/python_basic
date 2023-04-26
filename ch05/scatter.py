import statistics as st

def tot(lst):
    return sum(lst)

def avg(lst):
    return st.mean(lst)

def std(lst):       # 표준편차 : 각 값이 산술평균과 차이가 나는 값의 평균
    av = st.mean(lst)
    hap = 0.0
    for i in lst:
        hap = hap + (abs(i - av))
    vk = hap / len(lst)
    return vk

def vr(ls):     # 분산 : 표준편차의 제곱
    st = std(ls)
    return pow(st, 2)