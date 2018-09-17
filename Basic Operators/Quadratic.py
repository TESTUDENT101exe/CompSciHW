import math
a=float(input("Input a:"))
b=float(input("Input b:"))
c=float(input("Input c:"))
x=float(input("Input x:"))
aa=(2*a)
if (pow(b,2)-(4*a*c))>0:
    print("This quadratic has no solutions")
else:
    root=math.sqrt(((pow(b,2)-(4*a*c))))
    topA = -b+root
    topB= -b-root
    print((top1/aa),",",(top2/aa))


