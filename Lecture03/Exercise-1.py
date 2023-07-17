Frist_test_score = int(input('Enter the score for test 1: '))
Second_test_score = int(input('Enter the score for test 2: '))
Third_test_score = int(input('Enter the score for test 3: '))
average_score = (Frist_test_score+Second_test_score+Third_test_score) / 3
print('The average score is',average_score)
if average_score > 95:
    print('Congratulations!\nThat is a great average!')