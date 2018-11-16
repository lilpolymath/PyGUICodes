import math
y = 0

for n in range(1,100):
    y += 1
    for m in range(100):
        l = n**3 + m**3
        a = math.pow(l, 1/3)
        if a**3 =  n**3 + m**3:
            print("Match Found")
        print(n)
        print(a)
