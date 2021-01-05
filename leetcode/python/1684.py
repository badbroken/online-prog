allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]

count = 0
for i in [set(char) for char in words]:
    if i.issubset(set(allowed)):
        count += 1
print(count)
