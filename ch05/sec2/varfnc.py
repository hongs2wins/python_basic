# ch05 > sec2 > varfnc.py

def fnc1(a, b):                     # 일반함수
    print("데이터1 :", a, end="' ")
    print("데이터2 :", b)

def fnc2(a, *b):                     # 매개변수의 개수가 가변적인 -> 가변함수
    print("첫 번째 데이터 :",a)
    print("나머지 데이터 :",b)

def total(fnc, *data):
    if fnc == 'avg':
        return sum(data)/len(data)
    elif fnc =='sum':
        return sum(data)
    elif fnc =='max':
        return max(data)
    elif fnc == 'min':
        return min(data)
    else:
        return "Type Error"
