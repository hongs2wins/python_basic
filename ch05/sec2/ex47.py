import ch05.sec2.varfnc as fnc
# fnc.fnc1(1,"홍원준",90,80,100)  오류
fnc.fnc2(1,"홍원준",90,80,100)
# fnc.fnc1("홍원준","이순신","유관순")  오류
fnc.fnc2("홍원준","이순신","유관순")

print("평균 :", fnc.total("avg",90,75,80,95,100,85))
print("합계 :", fnc.total("sum",90,75,80,95,100,85))
print("최대값 :", fnc.total("max",90,75,80,95,100,85))
print("최소값 :", fnc.total("min",90,75,80,95,100,85))
print("기타 :", fnc.total("etc",90,75,80,95,100,85))

