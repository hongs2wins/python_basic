# ch02 > sec4 > ex17.py
# 문자열의 유형
linedata = "홍원준 입니다."
muldata1 = """홍원준은
멋있는
사람입니다."""
muldata2 = "홍원준 \n 멋있는 \n사람입니다."
print(linedata)
print("="*30)  # 문자열 반복 연산자
print(muldata1)
print("="*30)
print(muldata2)
print("="*30)
print("홍원준은"+"멋있는"+"사람입니다.")
# print("홍원준은"+1004+"입니다.") 문자열과 숫자는 서로 더할 수 없다.
print("원주율"+str(3.14))
print("원주율"+"3.14")

print("""홍원준은
멋있는 
사람입니다.""")