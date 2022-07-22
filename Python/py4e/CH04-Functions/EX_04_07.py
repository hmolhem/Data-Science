def computegrade(score):
    if score >= 0.9 and score <= 1:
        print('Grade: A')
    elif score >= 0.8 and score < 0.9:
        print('Grade: B')
    elif score >= 0.7 and score < 0.8:
        print('Grade: C')
    elif score >= 0.6 and score < 0.7:
        print('Grade: D')
    elif score >= 0 and score < 0.6:
        print('Grade: F')
    else: print('Bad score')

try:
    score = float(input('Enter Hours: '))
    flag = score >= 0 and score <= 1
except:
    print('Bad score')
    quit()
computegrade(score)
