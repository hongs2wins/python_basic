# ch03 > sec2 > ex30.py
# 이중 while문이나 for문을 활용하여 구구단을 출력
for i in range(1, 10):
    print("")
    for j in range(2, 10):
        print("%d*%d=%d" % (j, i, j*i), end="\t")


a = 1
while a<10:
    print("")
    b = 2
    while b<10:
        print("%d*%d=%d" % (b, a, b*a), end="\t")
        b = b + 1
    a = a + 1