#ch05 > sec3 > ex48.py

# lambda(람다) : 함수를 계산식화(표현식)화하여 사용
def add(x,y):
    return x+y
print(add(90,85))

def sub(x,y):
    return x-y
print(sub(90,85))

def mul(x,y):
    return x*y
print(mul(90,85))

def div(x,y):
    return x/y
print(div(90,85))

# 계산식도 한줄로만 표현가능
# 람다식 (lambda): 익명의 함수로 호출이 필요없이 처리하고자 할 경우 함수를 줄여 처리
print("Add :", (lambda x, y: x+y)(90,85))
print("Sub :", (lambda x, y: x-y)(90,85))
print("Mul :", (lambda x, y: x*y)(90,85))
print("Div :", (lambda x, y: x/y)(90,85))

