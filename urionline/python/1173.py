a = int(input())
z = []
for i in range(10):
    z.append(a)
    a *= 2
for j in range(len(z)):
    print("N[{}] = {}".format(j, z[j]))
