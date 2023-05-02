# 사용자 정의 모듈의 사용
import ch05.sec1.taekwondo as tk

hap = tk.sum(80, 90, 70)
py = tk.avg(80, 90, 70)
p1 = tk.kwa(80)
p2 = tk.kwa(90)
p3 = tk.kwa(70)
ps = tk.pan(80, 90, 70)
print("%d\t%d\t%d\t%d\t%3.2f\t%s" % (80, 90, 70, hap, py, ps))
print("서기 :", p1)
print("공격 :", p2)
print("막기 :", p3)