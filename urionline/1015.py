import math

def diff (a, b, c, d):
    asd = pow((c-a),2)+pow((d-b),2);
    print(round(math.sqrt(asd),4));


a,b = input().split();
c,d = input().split();
diff(float(a),float(b),float(c),float(d));