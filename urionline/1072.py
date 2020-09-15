x=0;
y=0;

def inter(a):
    global x, y;
    if a>= 10 and a<=20:
        x = x + 1;
    else:
        y = y + 1;
    print(x,"in");
    print(y,"out")

a=int(input());
for i in range(a):
    b = int(input());
    inter(b);