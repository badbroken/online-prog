def snack(x,y):
    if x==1:
        y=y*4.00
        print("Total: R$",format(float(y),'.2f'))
    elif x==2:
        y=y*4.50
        print("Total: R$",format(float(y),'.2f'))
    elif x==3:
        y=y*5.00
        print("Total: R$",format(float(y),'.2f'))
    elif x==4:
        y=y*2.00
        print("Total: R$",format(float(y),'.2f'))
    elif x==5:
        y=y*1.50
        print("Total: R$",format(float(y),'.2f'))

a,b=input().split()
snack(int(a),int(b))
