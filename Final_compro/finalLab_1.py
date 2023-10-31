def Gpacal(score):
    pre_gpa = 0
    sum_credits = 0
    subject = []
    Credits = {'Dismath':3,'Intro':3,'IntroLab':3,'Compro':3,'ComproLab':1,'SA':3,'Eng':3,'Human':3}
    for i in score.keys():
        subject.append(i)
    for k in subject:
        sum_credits += Credits[k]
        if score[k] >= 80:
            pre_gpa += 4*Credits[k]
        elif score[k] >= 75:
            pre_gpa += 3.5*Credits[k]
        elif score[k] >= 70:
            pre_gpa += 3*Credits[k]
        elif score[k] >= 65:
            pre_gpa += 2.5*Credits[k]
        elif score[k] >= 60:
            pre_gpa += 2*Credits[k]
        elif score[k] >= 55:
            pre_gpa += 1.5*Credits[k]
        elif score[k] >= 50:
            pre_gpa += 1*Credits[k]
        else:
            pre_gpa += 0*Credits[k]
    gpa = pre_gpa/sum_credits
    print(format(gpa,'.2f'))
    return format(gpa,'.2f')


Gpacal({'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79})