a = int(input());
b = list(map(int, input().split()))
p,q,r,s = 0,0,0,0;
for i in range(0,a):
    if b[i] % 2 == 0:
        p = p+1
    if b[i] % 3 == 0:
        q = q+1
    if b[i] % 4 == 0:
        r = r+1
    if b[i] % 5 == 0:
        s = s+1
print(p,"Multiplo(s) de 2")
print(q,"Multiplo(s) de 3")
print(r,"Multiplo(s) de 4")
print(s,"Multiplo(s) de 5")