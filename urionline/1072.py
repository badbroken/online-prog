x = 0
y = 0


def inter(m):
    global x, y
    if 10 <= m <= 20:
        x += 1
    else:
        y += 1


a = int(input())
for i in range(a):
    b = int(input())
    inter(b)
print(x, "in")
print(y, "out")