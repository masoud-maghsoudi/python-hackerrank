if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    records.sort(key = lambda x: x[1])
    
    record = []
    lowest_score_record = records[0]
    lowest_score = lowest_score_record[1]
    sec_lowest_name = []
    for record in records:
        if record[1] > lowest_score:
            sec_lowest_score = record[1]
            break
    for record in records:
        if sec_lowest_score == record[1]:
            sec_lowest_name.append(record[0])
    sec_lowest_name.sort()
    for output in sec_lowest_name:
        print(output)
