def time(a):
    h = a / 3600;
    b = a % 3600;
    m = b / 60;
    s = a % 60;
    print(b,m,s);
    s = "{}:{}:{}".format(int(h),int(m),s)
    print(s.replace(" ",""));

a=int(input())
time(a);