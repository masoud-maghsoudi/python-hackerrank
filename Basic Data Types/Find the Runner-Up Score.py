if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = []
    for score in arr:
        scores.append(score)
    scores.sort()
    best_score = scores[-1]
    runner_up_score = -100
    for score in scores:
        if score > runner_up_score and score < best_score:
            runner_up_score = score
    print(runner_up_score)
