#  ch04 > sec3 > ex39.py
res = [{'name':'kim','ko':90,'en':70,'ma':100,'tot':0,'avg':0.0},
       {'name':'lee','ko':80,'en':90,'ma':60,'tot':0,'avg':0.0},
       {'name':'park','ko':60,'en':70,'ma':100,'tot':0,'avg':0.0},
       {'name':'choi','ko':90,'en':60,'ma':90,'tot':0,'avg':0.0}]
# 위 데이터에서 총점(tot)와 평균(avg)을 구하여 출력하라
print("이름 \t총점\t평균")
for el in res:
       el["tot"] = el["ko"] + el["en"] + el["ma"]
       el["avg"] = float(el["tot"])/3.0
       print("%4s\t%d\t%f" % (el["name"], el["tot"], el["avg"]))

# 위 계산결과에서 평균에 따라 학점(hak)과 판정(pan)을 요소를 각 각 추가하고, 출력하라
# 학점 - 90이상:A, 80이상:B, 70이상:C, 60이상:D, 60미만:F
# 판정 - 평균이 70이상이면, "합격", 아니면, "불합격"




print("%4s\t%4s\t%4s" % ("이름","학점","판정"))
for el in res:
       if el["avg"] >= 90:
              el["hak"] = "A"
              el["pan"] = "합격"
       elif el["avg"] >= 80:
              el["hak"] = "B"
              el["pan"] = "합격"
       elif el["avg"] >= 70:
              el["hak"] = "C"
              el["pan"] = "합격"
       elif el["avg"] >= 60:
              el["hak"] = "D"
              el["pan"] = "불합격"
       else:
              el["hak"] = "F"
              el["pan"] = "불합격"
       print("%4s\t%4s\t%4s" % (el["name"], el["hak"], el["pan"]))