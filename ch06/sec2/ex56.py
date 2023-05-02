# ch07 > sec1 > ex56.py
# 정규 표현식 (Regular Expression =RegEx): 해당 데이터가 지정한 형태로 구성된
# 데이터인지 검증하는 식으로서 여러 메타 문자로 구성된다.
# 메타 문자 : 정규 표현식에서 일정한 의미를 같는 특수 문자

from re import compile, split, findall, sub
data='24512 kbs hwj홍원준 DEF_1234 서울특별시'
print(findall('1234', data))
print(findall('[0-9]',data))
print(findall('[가-힣]',data))
print(findall('[a-z]',data))
print(findall('[a-zA-Z]',data))
ls1=(findall('[a-zA-Z가-힣]{1,}',data))   #3글자부터
# print(findall('[a-zA-Z가-힣]{3}',data))   #3글자만 추출
print(ls1)
print(findall('^2',data))     # 문장의 시작이 2로 시작하는
print(findall('^kbs',data))     # 문장의 시작 kbs로 시작하는
print(findall('시$',data))       # 문장의 끝이 '시'로 끝나는
print(findall('서.',data))       # 접두사 서로 시작하여 .(한글자)
print(findall('.시',data))       # 접미다 시로 끝나는 .(한글자)

