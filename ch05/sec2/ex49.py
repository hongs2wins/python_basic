# ch05 > sec2 > ex49.py
# 재귀함수(self recursive function) : 반복문 없이 자기 자신 함수를 필요한 만큼 반복하여 실행

def rec(n):
    if n == 0:
        return 0
    else:
        rec(n-1)
    print(n)

rec(100)


def tot(n):
    if n == 1:
        return 1
    else:
        res = n + tot(n-1)
        return res

print("합계 :",tot(50))