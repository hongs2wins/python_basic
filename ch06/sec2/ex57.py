

from re import match
ju1 = "98123-3412345"
ju2 = "981230-3412345"
ju3 = "981230-341245"

def fnc1(ju):
    res1=match('[0-9]{6}-[0-9]{7}',ju)
    if res1:
        print(ju, "은 주민번호 패턴이 맞습니다.")
    else:
        print(ju, "은 주민번호 패턴이 아닙니다.")

fnc1(ju1)
fnc1(ju2)
fnc1(ju3)