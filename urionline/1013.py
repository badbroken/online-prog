def val(a,b,c):
    x=(a+b+abs(a-b))/2
    y=((x+c+abs(x-c))/2)
    print(int(y),"eh o maior")

a,b,c=input().split()
val(int(a),int(b),int(c))
