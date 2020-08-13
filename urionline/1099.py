def sum(a,b):
    val = 0;

    for i in range(a+1,b):
        if (i%2 !=0):
            val += i;
    print(val);

a=int(input());
for i in range(a):
    b,c = input().split()
    sum(int(b), int(c))