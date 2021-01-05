word1 = ["ab", "c"]
word2 = ["a", "bc"]
string1 = ""
string2 = ""
for item in word1:
    string1 += item
for item in word2:
    string2 += item
print(string2 == string1)
