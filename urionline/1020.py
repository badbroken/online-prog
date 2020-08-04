def age(a):
    y=a/365
    print(int(y),"ano(s)")
    x=(a-(365*int(y)))/30
    print(int(x),"mes(es)")
    z=(a-(365*int(y)))%30
    print(int(z),"dia(s)")
a=input()
age(int(a))
