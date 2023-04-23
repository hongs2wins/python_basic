# ch02 > sec4 > ex18.py
#문자열의 인덱스와 슬라이싱
data="Hongwonjun"
# 인덱스(Index) = 색인
print(data[0]) # 인덱스가 0인 글자
print(data[3]) # 인덱스가 3인 글자
print(data[-3]) # 인덱스가 -3(뒤에서부터 세번째)인 글자
print(data[-5]) # 인덱스가 -5(뒤에서 부터 다섯번째)인 글자

# 슬라이싱
print(data[0:5])    # 인덱스가 0부터 5전까지 begin:end[:step]
print(data[3:8])    # 인덱스가 3부터 8전까지
print(data[2:])     # 인덱스가 2부터 끝까지
print(data[:6])    # 인덱스가 처음부터 6전까지
print(data[:])      # 전체글자
print(data[-4:-2]) # 인덱스가 -4부터 -2전까지
print(data[-2:-4])  # 뒤에서부터는 슬라이싱을 할 수 없음
print("글자수 : ", len(data))
print(data[0::2])  # 인덱스가 0부터 끝까지 두 칸간격으로 슬라이싱
print(data[-10:-4:2]) # 인덱스가 -10부터 -4전까지 두 칸간격으로 슬라이싱


