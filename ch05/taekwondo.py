# ch05 > sec1 > taekwondo.py
# 태권도 승급처리 모듈을 만드시오. (모듈명 : taekwondo.py)
# 과목 - 서기(s : stand), 공격(a : attach), 막기(d : defence)
# 세 점수를 입력받아 총점(sum)을 계산하여 반환 -> sum
# 세 점수를 입력받아 평균(avg)을 계산하여 반환 -> avg
# 각 과목별 점수를 입력받아 70점 이상 받으면, "이수", 아니면 "미이수" 반환
# 세 점수가 모두 70점 이상이면, "승급성공", 아니면 "승급보류" 반환






def sum(s, a, d):       # 총점
    return s+a+d

def avg(s, a, d):       # 평균
    return (s+a+d)/3

def kwa(s):             # 과목별 이수사항
    if s>=70:
        return "이수"
    else:
        return "미이수"

def pan(s, a, d):       # 승급판정
    if s>=70 and a>=70 and d>=70:
        return "승급성공"
    else:
        return "승급보류"

