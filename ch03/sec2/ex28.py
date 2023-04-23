# ch03 > sec2 > ex29.py
# for문

'''
for 단일변수 in 컬렉션:
    반복실행할문장
'''
a = 100 # 기본형(단일기억장소)
lst = [90, 60, 95, 80, 85, 75]  # 참조형(collection)
lst2 =["홍원준", 42, 174, 4]
for i in lst:   # 컬렉션의 순회1 = 같은 타입의 집합체
    print(i)
for k in lst2:  # 컬렉션의 순회2 = 다른 타입의 집합체
    print(k)

'''
for 단일변수 in range():
    반복실행할문장
'''
# 0~100까지 합계
sum=0
for i in range(0,101):
    sum = sum+i
print("합산결과",sum)

# 0~100의 짝수의 합
sum=0
for i in range(0,101,2):
    sum=sum+i
print("짝수의 합산결과",sum)

# 0~100의 홀수의 합
sum=0
for i in range(1,101,2):
    sum=sum+i
print("홀수의 합산결과",sum)

for i in range(0, len(lst)):
    print(lst[i])