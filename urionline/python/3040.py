def chr(a,b,c):
    if a>=200 and a<=300 and b>=50 and c>=150:
        print("Sim");
    else:
        print("Nao");

a = int(input());
for i in range(a):
    a,b,c = input().split();
    chr(int(a),int(b),int(c))