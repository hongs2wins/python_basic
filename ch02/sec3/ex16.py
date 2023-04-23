# ch02 > sec3 > ex16.py
# 외부 상수에 의한 format 메소드로 출력
name="홍원준"
age=50
ht=175.5
# 상수의 자동배치
print("이름: {}, 나이: {}, 키:  {}".format(name,age,ht))
# 상수의 인덱스에 의한 배치
print("이름: {1}, 나이: {2}, 키: {0}".format(ht,name,age))
# 형식지시자의 변수명에 의한 배치
print(f"이름: {name}, 나이: {age}, 키: {ht}")