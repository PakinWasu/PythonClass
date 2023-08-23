def capToFront(text):
    tt = ''
    #print(text.isupper())
    for t in text:
        #print(t)
        if t.isupper() == True:
            tt = tt+t
    for t in text:
        #print(t)
        if t.islower() == True:
            tt = tt+t
    
    return(tt)

print(capToFront('hApPy'))
print(capToFront('moveMENT'))
print(capToFront('shOrtCAKE'))
