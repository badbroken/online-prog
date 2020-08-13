# def bank(a):
#     print("NOTAS:")
#     p=float(a)/100
#     print(int(p),"nota(s) de R$ 100.00")
#     q=(float(a)-(int(p)*100))/50
#     print(int(q),"nota(s) de R$ 50.00")
#     r=(float(a)-(int(p)*100)-(int(q)*50))/20
#     print(int(r),"nota(s) de R$ 20.00")
#     s=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20))/10
#     print(int(s),"nota(s) de R$ 10.00")
#     t=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10))/5
#     print(int(t),"nota(s) de R$ 5.00")
#     u=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5))/2
#     print(int(u),"nota(s) de R$ 2.00")
#     print("MOEDAS:")
#     b=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2))/1
#     print(int(b),"moeda(s) de R$ 1.00")
#     c=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1))/0.50
#     print(int(c),"moeda(s) de R$ 0.50")
#     d=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50))/0.25
#     print(int(d),"moeda(s) de R$ 0.25")
#     e=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50)-(int(d)*0.25))/0.10
#     print(int(e),"moeda(s) de R$ 0.10")
#     f=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50)-(int(d)*0.25)-(int(e)*0.10))/0.05
#     print(int(f),"moeda(s) de R$ 0.05")
#     g=(float(a)-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50)-(int(d)*0.25)-(int(e)*0.10)-(int(f)*0.05))/0.01
#     print(int(g),"moeda(s) de R$ 0.01")
# a=input()
# bank(a)

def bank(a):
    print("NOTAS:")
    p=a/100
    print(int(p),"nota(s) de R$ 100.00")
    q=(a-(int(p)*100))/50
    print(int(q),"nota(s) de R$ 50.00")
    r=(a-(int(p)*100)-(int(q)*50))/20
    print(int(r),"nota(s) de R$ 20.00")
    s=(a-(int(p)*100)-(int(q)*50)-(int(r)*20))/10
    print(int(s),"nota(s) de R$ 10.00")
    t=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10))/5
    print(int(t),"nota(s) de R$ 5.00")
    u=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5))/2
    print(int(u),"nota(s) de R$ 2.00")
    print("MOEDAS:")
    b=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2))/1
    print(int(b),"moeda(s) de R$ 1.00")
    c=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1))/0.50
    print(int(c),"moeda(s) de R$ 0.50")
    d=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50))/0.25
    print(int(d),"moeda(s) de R$ 0.25")
    e=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50)-(int(d)*0.25))/0.10
    print(int(e),"moeda(s) de R$ 0.10")
    f=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50)-(int(d)*0.25)-(int(e)*0.10))/0.05
    print(int(f),"moeda(s) de R$ 0.05")
    g=(a-(int(p)*100)-(int(q)*50)-(int(r)*20)-(int(s)*10)-(int(t)*5)-(int(u)*2)-(int(b)*1)-(int(c)*0.50)-(int(d)*0.25)-(int(e)*0.10)-(int(f)*0.05))/0.01
    print(int(g),"moeda(s) de R$ 0.01")
a=input()
bank(float(a))