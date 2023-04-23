# ch03 > sec2 > ex29.py
# 무한 while을 활용하여 입출금 시스템을 프로그래밍하라.

balance =0  # 잔액
while True:
    job = int(input("작업할 번호[1.입금, 2.출금, 3.조회, 4.종료"))
    if job==1:
        money = int(input("입금할 금액 입력 :"))
        balance = balance + money
    elif job==2:
        money = int(input("출금할 금액 입력 :"))
        if money>balance:
            print("잔액부족 : 출금할 금액이 잔액 보다 더 큽니다.")
        else:
            balance = balance - money
    elif job==3:
        print("현재 잔액 :",format(balance,"3,d"))
    else:
        print("프로그램을 종료합니다.")
        break

