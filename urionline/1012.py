def sp(a,b,c):
    x=(1/2)*float(a)*float(c)
    print("TRIANGULO:",format(float(x),'.3f'))
    y=3.14159*float(c)**2
    print("CIRCULO:",format(float(y),'.3f'))
    z=(float(a)+float(b))*float(c)/2
    print("TRAPEZIO:",format(float(z),'.3f'))
    p=float(b)**2
    print("QUADRADO:",format(float(p),'.3f'))
    q=float(a)*float(b)
    print("RETANGULO:",format(float(q),'.3f'))

(a,b,c)=input().split()
sp(a,b,c)
