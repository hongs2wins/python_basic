# ch06 > sec1 > ex51.py
from ch06.sec1.travel import Flight
f1=Flight('대한항공',1200000, 14)
f1.prt()
f1=Flight('아시아나',110000,14)
f1.prt()
f1=Flight('제주항공',80000,14)
f1.prt()

print("f1의 타입:",type(f1))