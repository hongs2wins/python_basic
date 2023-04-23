# ch04 > sec1 > ex33.py
# 중첩 리스트 : 2차원 이상의 리스트
ls1 = [[30,60],[20,70],[40,30,50],[10,80]]
print("중첩 리스트 :", ls1)
print("중첩 리스트 요소 행의 개수 :", len(ls1))
print("중첩 리스트 0번째 행의 컬럼 개수 :", len(ls1[0]))
print("중첩 리스트 2번째 행의 컬럼 개수 :", len(ls1[2]))

print("차원 축소")
# 차원 축소 = 평탄화(2차원 -> 1차원)
ls2 = sum(ls1, [])
print("ls2 :", ls2)

# 이중 for문
ls3 = []
for inner in ls1:
    for j in inner:
        ls3.append(j)
print("ls3 :", ls3)

# 이중 내포문
ls4 = [j for inner in ls1 for j in inner]
print("ls4 :", ls4)

# numpy, pandas => 외부 라이브러리 : 설치 필요
import numpy as np
ls5 = np.concatenate(ls1).tolist()
print("ls5 :", ls5)

# itertools, reduce => 내장 라이브러리
import itertools
ls6 = list(itertools.chain(*ls1))
ls7 = list(itertools.chain.from_iterable(ls1))
print("ls6 :", ls6)
print("ls7 :", ls7)

from functools import reduce
import operator
ls8 = list(reduce(operator.add, ls1))
print("ls8 :", ls8)




