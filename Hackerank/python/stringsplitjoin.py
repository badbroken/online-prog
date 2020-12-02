def split_and_join(a):
    a = a.split(" ")
    a = "-".join(a)
    return a



line = input()
result = split_and_join(line)
print(result)
