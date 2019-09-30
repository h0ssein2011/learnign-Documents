if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum_scores=sum(student_marks[query_name])
N_scores=len(student_marks[query_name])
print("%.2f" % (sum_scores / N_scores))
