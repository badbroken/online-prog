if __name__ == '__main__':
    # n = int(input())
    n = 2
    student_marks = {'Harsh': [25.0, 26.5, 28.0], 'Anurag': [26.0, 28.0, 30.0]}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    query_name = 'Harsh'

for k, v in student_marks.items():
    if k == query_name:
        print(format(sum(v) / len(v), '.2f'))
