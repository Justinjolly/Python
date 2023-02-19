import math
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))
d = (b*b)-(4*a*c)
if d == 0:
    print("Roots are identical")
    r1=r2=(-b)/(2*a)
    print('r1='+r1 +' r2 ='+r2)
elif d>0:
    print("roots are real")
    r1 = -b + math.pi(d) / (2 * a)
    r2 = -b + math.pi(d) / (2 * a)
    print('r1=' + r1 + ' r2 =' + r2)
else:
    print("roots are imaginary")



