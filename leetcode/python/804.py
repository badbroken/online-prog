morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

words = ["gin", "zen", "gig", "msg"]
unique_morse_set = []
for i in words:
    string = ""
    for j in [char for char in i]:
        string += morse_code[ord(j) - 97]
    unique_morse_set.append(string)

print(len(set(unique_morse_set)))
