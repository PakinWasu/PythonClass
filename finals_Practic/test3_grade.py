criterion = {'A':80,'B+':75,'B':70,'C+':65,'C':60,'D+':55,'D':50,'F':0}
subject = {'Dismath':3,'Intro':3,'IntroLab':3,'Compro':3,'ComproLab':1,'SA':3,'Eng':3,'Human':3}
studens = {'Boss':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Chin':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Vas' :{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Jez' :{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Tub' :{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79}, 
           'Nine':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79}, 
           }
subject_key = []
num_criterion={'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}

def grade(name):
    subject_key = []
    gpx = 0
    sum_num_criterion = 0
    for i in subject.keys():
        subject_key.append(i)
    score_studen = studens[name]
    print('Grade',name) 
    
    for k in subject_key:
        sum_num_criterion += subject[k]
        if score_studen[k] >= criterion['A']:
            gpx += (num_criterion['A']*subject[k])
            print(k,':','A')
        elif score_studen[k] >= criterion['B+']:
            gpx += (num_criterion['B+']*subject[k])            
            print(k,':','B+')
        elif score_studen[k] >= criterion['B']:
            gpx += (num_criterion['B']*subject[k]) 
            print(k,':','B')
        elif score_studen[k] >= criterion['C+']:
            gpx += (num_criterion['C+']*subject[k]) 
            print(k,':','C+')
        elif score_studen[k] >= criterion['C']:
            gpx += (num_criterion['C']*subject[k]) 
            print(k,':','C')  
        elif score_studen[k] >= criterion['D+']:
            gpx += (num_criterion['D+']*subject[k]) 
            print(k,':','D+')
        elif score_studen[k] >= criterion['D']:
            gpx += (num_criterion['D']*subject[k]) 
            print(k,':','D')        
        else:
            gpx += (num_criterion['F']*subject[k]) 
            print(k,': F')        
        #print(k)
    print('GPX :',format(gpx/sum_num_criterion,'.2f'))

grade('Boss')

#OUTPUT
# Grade Boss 
# Dismath : A
# Intro : A
# IntroLab : A
# Compro : A
# ComproLab : A
# SA : A 
# Eng : A 
# Human : B 
#GPX : 3.92

#*****GPX = ((เกรด*หน่วยกิต)(เกรด*หน่วยกิต)(เกรด*หน่วยกิต)(เกรด*หน่วยกิต))/หน่วยกิตรวม