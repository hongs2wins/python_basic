# ch04 > sec2 > ex36.py
# 딕셔너리(Dictionary = dict)
# 1. 키의 중복은 불허, 값의 중복은 허용
# 2. 키로 값을 구분하는 비순서형임
# 3. 키와 값의 쌍으로 데이터를 제공함
# 4. 선언시 {로 시작하고, }로 끝남
d1 = {'name':'김기태', 'age':42, 'height':174.5, 'weight':72.9}
print(d1, "요소수 :",len(d1), "타입 :", type(d1), "주소 :", id(d1))
d2 = dict(a=100, b=70, c=90)
print(d2, "요소수 :",len(d2), "타입 :", type(d2), "주소 :", id(d2))

d3 = d1.copy()
print(d3, "요소수 :",len(d3), "타입 :", type(d3))
d3.update(d2)       # 딕셔너리 합치기(d1에 d1와 d2를 합친 값을 대입)
print(d3, "요소수 :",len(d3), "타입 :", type(d3))
d3["d"] = 60        # 특정 키(원소) 접근하여 키와 값 추가
print(d3, "요소수 :",len(d3), "타입 :", type(d3))
d3["age"] = 31      # 특정 키(원소) 접근하여 값 변경
print(d3, "요소수 :",len(d3), "타입 :", type(d3))

print("d3의 키만 접근 :", d3.keys(), "\n키의 개수 :", len(d3))
print("d3의 값만 접근 :", d3.values())
d4 = d3.items()        # 키와 값
print("d3의 키와 값의 동시 접근 :", d3.items(), "\n키의 개수 :", len(d3))
# dictionary의 items는 튜플의 리스트
del d3["b"]         # 특정 키와 값 제거
print(d3, "\n아이템의 개수 :", len(d3))
d3.clear()          # 딕셔너리 비우기
print(d3, "\n아이템의 개수 :", len(d3))

# 딕셔너리의 순회
a = {"name":"kim", "hobby":"fishing", "address":"deokyanggu, goyang city"}
for key, value in a.items():
    print("key :", key, end=", ")
    print("value :", value)

# 키와 값을 분류하여 각 각 튜플로 변환하여 저장
t1 = tuple(a.keys())
t2 = tuple(a.values())
print("a의 키를 튜플로 변환 :", t1)
print("a의 값을 튜플로 변환 :", t2)

# 이중 컬렉션 프레임워크
# 외부는 리스트, 내부는 딕셔너리
b = [{'name':'kim', 'age':25}, {'name':'lee', 'age':31}]
c = {'name':'park', 'age':27}
b.append(c)
print(b, "\n인원수 :", len(b))
print(b[0], "\n항목수 : ", len(b[0]))

for el in b:
    for key, value in el.items():
        print("항목명 :", key, end=", ")
        print("값 :", value)
    print()
    
# name이 lee인 데이터의 키와 값만 출력
for el in b:
    if el['name']=='lee':
        for key, value in el.items():
            print(key, end=":")
            print(value)