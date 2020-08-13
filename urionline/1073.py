def sqr(a):
    for i in range(1,a+1):
        if i%2 == 0:
            print("{}^{} =".format(i,i),i**2)
a=int(input())
sqr(a)