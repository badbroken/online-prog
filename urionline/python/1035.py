def sel(a,b,c,d):
    if b > c and d > a and (c+d) > (a+b) and a%2 == 0 and c > 0 and d > 0:
        print("Valores aceitos");
    else:
        print("Valores nao aceitos")

a,b,c,d = input().split();
sel(int(a),int(b),int(c),int(d));