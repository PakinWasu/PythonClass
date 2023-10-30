def con_eng(*num):
    #print(num)
    msg = ''
    eng = {}
    for i in range(1,26+1):
        eng.update({i:chr(64+i)})
    #print(eng)
    for  k in num:
        #print(k)
        msg += eng[k]
    return msg
print(con_eng(1,14,20))#output: ANT
print(con_eng(9,16,1,4))#output: IPAD
print(con_eng(16,25,20,8,15,14))#output: PYTHON