# ch03 > sec2 > ex27.py

'''
do~while : 적어도 한 번 이상 실행해야 하는 구조의 문장
'''

n = 0
while True:
    n = n + 1
    print("n=%d" % n)
    if n >= 0:
        break

'''
이중반복
'''

a=0
b=0
while a<5:
    a=a+1
    print("")
    b=0
    while b<3:
        b=b+1
        print(b, end="")        # a=1:b=1# a=2:b=1~3~~ 15번 실행