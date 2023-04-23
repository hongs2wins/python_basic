# ch02 > sec3 > ex14.py
# format 문자 : print("%코드양식" % 변수명)
name = "홍원준" # 문자 %s
age=50  # 10진수 정수 %d
hobby="coding"    # 문자 %s
ht=175.5    # 실수 %f
wt=82.2     # 실수 %f
print("이름: %s" %name)
print("나이 : %d" %age)
print("키: %f" %ht)
print("취미 : %s" %hobby)
print("이름 : %s, 나이 : %d 키, : %f, 몸무게 : %f" %(name,age,ht,wt))


num=int(input("변환할 숫자 입력 :"))
print("10진수 : %d, 8진수 : %o, 16진수 : %x" %(num,num,num),end=", ")
print("2진수 :",bin(num))

product=input("구매할상품명 :")
price=4500
su=int(input("구매수량 :"))
ds=0.12
total=su*price*(1-ds)
print("상품명: %s, 단가 : %d, 구매수량 : %d, 총금액 : %.2f, 할인율 : %.2f" %(product,price,su,total,ds))