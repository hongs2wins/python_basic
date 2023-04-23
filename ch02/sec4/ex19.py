# ch02 > sec4 >ex19.py
# 문자열 관련 함수
data = "         HongWonJun          "
print("글자수 : ",len(data))
print("대문자로 변경:", data.upper())
print("소문자로 변경:",data.lower())
print("대문자는 소문자로 소문자는 대문자로:",data.swapcase())
print("앞의 공백제거:",data.lstrip(),len(data.lstrip()))
print("뒤의 공백제거:",data.rstrip(),len(data.rstrip()))
data2= data.strip()
print("첫 글자 대문자, 나머지는 소문자:",data2.capitalize()) # 첫글자만 대문자로
print("o 글자의 개수:",data2.count('i'),"개")
print("o자의 위치 : 인덱스",data2.find('i'),"번째") # 처음 발견한 위치 리턴
print("o자의 위치 : 인덱스",data2.rfind('o'),"번째") # 맨 나중에 발견한 위치 리턴
# print("o자의 위치 : 인덱스",data2.index('i'),'"번째') # 처음 발견한 위치 리턴 (못 찾으면 오류)
data3=data2.replace("W","K") # 대소문자 구분함(find,rfind,index,replace)
print("W를 K로 찾아 바꾸기",data3)
print("K로 시작하는지 여부",data2.startswith('K'))
print("n로 끝나는지 여부:",data2.endswith('n'))

