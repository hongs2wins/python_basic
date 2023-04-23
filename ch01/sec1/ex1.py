# project1 > ch01 > sec1 > ex1.py
print("Hello World")
# 변수 : 데이터 저장 목적으로 알기 힘든 16진수 주소대신 알기 쉬운 별명을 붙인 것
a = 100     # int a = 100;
b = 3.14    # float b = 3.14f;
c = "김기태"   # c라는 기억장소에 "김기태" 저장하라
d = True
e = a + b
# f = a + c   # typeError
print("a=", a, type(a), id(a))  # a : int
print("b=", b, type(b), id(b))  # b : float
print("c=", c, type(c), id(c))  # c : str
print("d=", d, type(d), id(d))  # d : bool
print("e=", e, type(e), id(e))  # e : float
# print("f=", f, type(f), id(f))  # f : type Error
school = 1004
School = 1004

import keyword
py_word = keyword.kwlist
print(py_word)

# 관례
# 변수명은 영문 소문자로 시작
# 가급적 변수명의 그 의미나 용도를 쉽게 알 수 있게 지정
# 여러 단어를 조합하여 변수명을 명명할 때 카멜방식 또는 스네이크 방식으로
# 조합할 것

# winteragenumber(X)
# winterAgeNumber(O) - 카멜 방식
# winter_age_number(O) - 스네이크 방식