import math;
def bha(a,b,c):
    x=(-b+math.sqrt(b**2-(4*a*c)))/2*a
    y=(-b-math.sqrt(b**2-(4*a*c)))/2*a
    print("R1 =",round(x/100,5))
    print("R2 =",round(y/100,5))

a,b,c=input().split()
bha(float(a), float(b), float(c))