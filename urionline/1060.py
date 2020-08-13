val = 0;

def pos(a):
    global val
    if a>0:
        val += 1



for i in range(6):
    a = float(input());
    pos(a);
print(val,"valores positivos");