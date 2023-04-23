# ch04 > sec3 > ex38.py

data = ["cat", "dog", "hen", "cat", "egle", "dog", "fish", "cat", "hen"]
# 위 데이터에서 중복을 제거한 요소를 출력하고, 개수를 출력하라
data = set(data)
print(data, "개수 :",len(data))

lst = [{'name':'kim'}, {'name':'lee'}, {'name':'park'}, {'name':'choi'}]
# 위 데이터에서 name의 값만 추출하여 출력하라
for el in lst:
    for key, value in el.items():
        print(value)






