# ch04 > sec1 > ex31.py

# 컬렉션 프레임워크 : 하나의 데이터가 아닌 여러 데이터를 한 곳에 모아
# 저장하여 관리하는 저장소 데이터 타입
# 종류 : 리스트(List), 튜플(Tuple), 셋(Set), 딕셔너리(Dictionary)
# 리스트(List)
# 1. 순서적인 자료이며, 자료의 중복이 허용됨 => 인덱스 0
# 2. 가변형 자료 구조로서 자유롭게 요소를 제거나 추가할 수 있음
# 3. 자료 구조의 연산이 가능
# 4. 읽고 쓰는 것이 자유롭다.
# 5. 선업 및 구분자는 [ 로 시작하고 ]로 닫는다.

lst1 = [40, 80, 20, 70, 60]     # 정수 자료형 리스트
lst2 = ['kim','park', 'choi', 'lee']  # 문자열 자료형 리스트
lst3 = ['kim', 42, 174, True]   # 여러 기본 자료형
print(lst1, "요소의 수 :", len(lst1))
print(lst2,"요소의 수 : ", len(lst2))
print(lst3, "요소의 수 :", len(lst3))

lst4=[]  # 빈 리스트 선언 또는 lst4 = list()
print(lst1, "요소의 수1 :", len(lst1))
lst1.append(50)                     #요소를 가장 끝에 추가
print(lst1, "요소의 수2:", len(lst1))
print("세 번째 요소 :",lst1[2])      # 인덱스가 2인 요소의 접근
lst1[3] =75                         # 인덱스가 3인 요소의 값 변경
lst1.insert(1,65)                  # 특정 위치에 요소를 추가
print(lst1, "요소의 수3", len(lst1))
lst1.remove(75)                     # 특정 요소를 제거
print(lst1, "요소의 수4 :", len(lst1))
print(lst1.pop())                   # 끝 요소(tail)를 반환 후 제거
print(lst1, "요소의 수5 :",len(lst1))
print("최대값:",max(lst1))
print("최소값:",min(lst1))
# lst1=lst1+lst2                     # 리스트 합치기 연산
# lst1=extend(lst2)                  # 리스트 합치기 확장
lst1.append(65)                      #  요소의 가장 끝에 추가
print(lst1, "요소의 수6 :",len(lst1))
print("lst1의 20의 위치 :",lst1.index(20))
print("lst1에서 20의 개수 :",lst1.count(20))

# 깉은 복제 : 다른 주소에 데이터를 복제하는 것이므로, 별개의 데이터로 존재함
copy_lst = lst1.copy()
#얕은 복제 : 같은 주소에 있는 데이터를 공유하므로, 어느 한 곳에 데이터를 변경하면, 같이 변경됨
data_lst = lst1
print( lst1, "lst 요소의 수:", len(lst1), "메모리 주소 :",id(lst1))
print( copy_lst, "copy_lst 요소의 수:", len(copy_lst), "메모리 주소 :",id(copy_lst))
print( data_lst, "data_lst 요소의 수:", len(data_lst), "메모리 주소 :",id(data_lst))
lst1.sort()         # 올림차수 정렬
print("정렬된 리스트 : ",lst1)
lst2.sort()
lst4=lst1+lst2
lst4.sort()         #문자열과 숫자는 혼합은 가능하지만 혼합된 데이터는 정렬 할 수 없음

lst1 = [40, 80, 20, 70, 60]     # 정수 자료형 리스트
lst2 = ['kim','park', 'choi', 'lee']  # 문자열 자료형 리스트

lst1.reverse()
lst2.reverse()
print("lst1 :",lst1)
print("lst2 :",lst2)
lst2.clear()            # 리스트 비우기
print("lst2 :", lst2)
lst5 = lst1[1:3]    # 리스트 슬라이싱 - 인덱스가 1부터3전 까지
lst6 = lst1[:4]     # 리스트 슬라이싱 - 인덱스가 4전까지
lst7 = lst1[2:]     # 리스트 슬라이싱 - 인덱스가 2부터 끝 까지
print("lst1 :",lst1)
print("lst5 :",lst5)
print("lst6 :",lst6)
print("lst7 :",lst7)
help(list)
