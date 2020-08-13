def ran(a):
    if a==0:
        print("E");
    elif a>=1 and a<=35:
        print("D");
    elif a>=36 and a<=60:
        print("C")
    elif a>=61 and a<=85:
        print("B")
    elif a>=86 and a<=100:
        print("A")
    
a=int(input());
ran(a);