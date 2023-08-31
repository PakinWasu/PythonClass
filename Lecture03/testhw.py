# for muti in range(27,31):
#     print('-------------')
#     print('     %d      '%muti)
#     print('-------------')
#     for num in range(1,13,1):
#         sum = muti * num
#         print(f"{muti:>2} x {num:>2} = {sum:>3}")
#     print()


#first draf
#def muti_table (muti):
    # column = 4
    # row = 12
    # roww = row+1
    # heading = ''
    # for head in range(muti,muti+column):
    #     heading = heading+"     "+f"{head:>3}"+"\t"
    # print(heading)

    # for num in range(1,roww,1):
    #     col = 0
    #     for i in range(muti,muti+column) :
    #         sum = i * num
    #         print(f"{i:>2} x {num:>2} = {sum:>3}",end=' | ')
    #         col = col + 1
    #         if(col == column):
    #             print('')      
    # return ""

def muti_table (muti,column,row):
    #head
    heading = ''
    for head in range(muti,muti+column):
        heading = heading+"|"+"     "+f"{head:>3}"+"      | "
    print(heading)

    #table
    for num in range(1,row+1,1):
        col = 0
        for i in range(muti,muti+column) :
            sum = i * num
            print("|"+f"{i:>2} x {num:>2} = {sum:>3}",end=' | ')
            col = col + 1
            if(col == column):
                print('')      
    return ""

def muti_table_up (muti_min,muti_max,column,row):
    #หาส่วนว่าต้องทำเต็มคอลัมที่กำหนดกี่รอบ
    r = ((muti_max-muti_min)+1)//column
    #หาเศษว่าเหลือเท่าไหร่ ใช้บอกว่าเหลืออีกกี่คอลัมถึงจะครบ max
    rr = ((muti_max-muti_min)+1)%column
    #print(r,rr)
    for i in range(0,r):
        print(muti_table(muti_min,column,row))
        muti_min = muti_min + column
    if ((muti_max-muti_min)+1)%column != 0 :
        print(muti_table(muti_min,rr,row))
    return ""
print(muti_table_up(27,39,4,13))

#print(muti_table(27,4,12))


