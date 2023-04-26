# ch05 > sec1 > ex41.py
# 모듈과 패키지
# 모듈 : 파이썬 파일 하나 => ex41
# 패키지 : 관련 있는 모듈을 하나의 디렉토리 개념으로 묶은 것. => sec1
# 내장 모듈 : 파이썬 설치시 기본으로 파이썬에 내장되는 py 파일
# 외장 모듈 : 별도로 제공되는 라이브러리나 사용자가 작성한 py 파일
# builtins 모듈 : 내장 모듈 중에서 별도의 import 없이 사용 가능한 모듈
# import 모듈 : 내장 모듈 중에서 별도의 import 가 필요한 모듈
# list(), int(), tuple(), id(), len(),....
# import : 외장(외부) 모듈이나 불틴이 아닌 모듈을 가져오기
# 모듈의 구성 : 여러 함수로 구성되어 있음
# import 모듈명
# import statistics   statistics 모듈을 한 꺼번에 불러올 경우 활용
#import statistics as st   statistics 모듈명을 st로 줄여서 알리아스로 불러올 경우 활용
# from 모듈명 import 함수명1,....
# from statistics import stdev, median, mode  # statistics 모듈에서 필요한 stdev, median, mode 함수만 불러오는 경우
import statistics
lst = [70, 100, 90, 85, 75, 95, 100]
print(lst)
print("개수 : ", len(lst))        # builtins 함수
print("메모리 주소 : ", id(lst))
print("타입 : ", type(lst))
print("합계 : ", sum(lst))
print("최대값 : ", max(lst))
print("최대값 : ", min(lst))
print("분산 :", statistics.variance(lst)) # import 함수
print("표준편차 :", statistics.stdev(lst))

from statistics import median, mode, mean, harmonic_mean, geometric_mean
print("중간값 : ", median(lst))
print("최빈수 : ", mode(lst))
print("산술평균 : ", mean(lst))
print("조화평균 : ", harmonic_mean(lst))
print("기하평균 : ", geometric_mean(lst))

# builtins 함수 보기 : 118 페이지 참고
import builtins as bt
print(dir(bt))


