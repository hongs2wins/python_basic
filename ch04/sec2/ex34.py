# ch04 > sec2 > ex34.py
# 튜플(Tuple) : 불변형 컬렉션 프레임워크
# 1. 요소의 추가 및 삭제 등 편집이 불가능한 일기 전용임
# 2. 요소에 순서가 있음 => 인덱스가 존재
# 3. 튜플끼리의 연산 가능
# 4. 자료를 보존할 이유가 잇는 경우에 활용
# 5. 선언시(로 시작하고,) 로 끝남

tp1 =(60, 80, 70, 90, 100, 65)
lst1 = [60, 80, 70, 90, 100]

lst1.append(65)
print("tp1", tp1, "개수 :",len(tp1))
print("lst1",lst1,"개수 :",len(lst1))
print("tp1의 타입 :",type(tp1))
print("lst1의 타입 :",type(lst1))
print("lst1에서 65의 개수 :",lst1.count(65))
print("tp1에서 65의 개수 :",tp1.count(65))
print("lst1에서 인덱스가 2인 요소 :",lst1[2])
print("tp1에서 인덱스가 2인 요소 :",tp1[2])
print("lst1에서 90의 위치 :",lst1.index(90))
print("tp1에서 90의 위치 :",tp1.index(90))
print("lst1에서 최대값 :",max(lst1))
print('tp1에서 최대값 :',max(tp1))
print("lst1에서 최소값 :",min(lst1))
print("tp1에서 최소값 :",min(tp1))

# 튜플에서 요소를 추가
tp1 = list(tp1)     # 리스트화
tp1.append(75)
tp1=tuple(tp1)      # 튜플화
print("tp1에서 75를 추가 :",tp1)

tp2 = (85, 75,90, 95, 60)
tp3 = tp1 + tp2
print("tp1 :", tp1)
print("tp2 :",tp2)
print("tp3 :",tp3)