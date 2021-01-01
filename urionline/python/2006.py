a = int(input())
t = 0
p = input().split()
for i in range(5):
    if int(p[i]) == int(a):
        t += 1
print(t)