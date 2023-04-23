lst1 = [75, 80, 90, 70, 65, 85]
print("lst1 :",lst1)
print("lst1 요소의 수 :",len(lst1))
print("lst1 주소 :",id(lst1))
print("lst1 자료형 :",type(lst1))

# 리스트의 순회
for i in lst1:
    print("데이터 요소 :",i)

# 리스트의 요소 연산
sq1=[]
for i in lst1:
    sq1.append(i*i)
print("sq1 :",sq1)

'''sq1=[]
for i in lst1:
    sq1.append(i*i)
    print("sq1 :",sq1)'''

# 리스트의 요소 연산 내포문
sq2 = [i*i for i in lst1]       # [계산식 for 변수 in 컬렉션]
print("sq2 :",sq2)

# 짝수만 담기
print(lst1)
an1 = []
for i in lst1:
    if i % 2 ==0:
        an1.append(i)
print("an1 :",an1)

# 조건 내포문 : [계산식 for 변수 in 컬렉션 if 조건식]
an2 = [i for i in lst1 if i%2==0]
print("an2 :", an2)

# lst1의 요소에서 75 이상이면, 값+2, 미만이면 값-2
dv1=[]
for i in lst1:
    if i>=75:
        dv1.append(i+2)
    else:
        dv1.append(i-2)
print("dv1 :",dv1)

# [계산식1 if 조건식 else 계산식2 for 변수 in 컬렉션]
dv2 =[i+2 if i>75 else i-2 for i in lst1]
print("dv2 :",dv2)