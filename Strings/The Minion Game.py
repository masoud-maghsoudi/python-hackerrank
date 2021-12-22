def minion_game(string):
    vowels = ('A','E','I','O','U')
    kev_score, stu_score = 0, 0
    for i in range(len(string)):
        if string[i] in vowels:
            kev_score += (len(string)-i)
        else:
            stu_score += (len(string)-i)
    if (kev_score > stu_score):
        print("Kevin {}".format(kev_score))
    elif(kev_score < stu_score):
        print("Stuart {}".format(stu_score))
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
