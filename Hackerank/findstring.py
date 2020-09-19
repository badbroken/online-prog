def count_substring(a, b):
    return a.count(b)


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

# a = str(input())
# b = str(input())
# findstring(a, b)
