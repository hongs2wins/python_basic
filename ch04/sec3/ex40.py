# ch04 > sec3 > ex40

# 최대값, 최소값 알고리즘
arr = [90, 70, 75, 80, 85, 60, 95, 65]
max = 0
min = 100
for i in arr:
    # 최대값보다 크면,
    if i>max:
        max = i
    # 최소값보다 작으면,
    if i<min:
        min = i
print("최대값 : ",max)
print("최소값 : ",min)

# 정렬 알고리즘 : 특정 값과 나머지 값들을 순차적으로 비교하여
# 그 특정 값이 더 크면, 자리를 교체함
# selection sort(선택 정렬)
arr = [90, 70, 75, 80, 85, 60, 95, 65]
n = len(arr)
for i in range(0, n-1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

