if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    scores = student_marks[query_name]
    score_count = len(scores)
    score_total = float(0)
    for score in scores:
        if score:
            score_total += score
    print("{:.2f}".format(score_total/score_count))
