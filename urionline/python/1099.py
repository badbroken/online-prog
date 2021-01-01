val = []


def summ(a, b):
    for i in range(b + 1, a):
        if i % 2 != 0:
            val.append(str(i))


x = []
a = int(input())
for i in range(a):
    b = input().split()
    for j in range(len(b)):
        x.append(b[j])
    x.sort(reverse=True)
    summ(int(x[-2]), int(x[-1]))
    x.clear()
print(val)
# print(*val, sep="\n")
