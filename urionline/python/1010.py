a,b,c = map(float, input().split());
x,y,z = map(float, input().split());
p = b*c;
q = y*z;

print("VALOR A PAGAR: R$", format(p+q,'.2f'));