# โค้ดสอบ
m = [31,28,31,30,31,30,31,31,30,31,30,31]
def what_day_month (dd,mm) :
    n = 0
    sumday = 0
    for i in m :
        if n == mm-1 :
            break
        n = n+1
        sumday = sumday + i
    sumday = sumday + dd
   
    first_day_month = (sumday - 2)%7
    return(first_day_month)

mm = int(input('Enter Month : '))
first_day = what_day_month(1,mm)

print('='*20)
print("M  T  W  T  F  S  S")
print('='*20)
for i in range(first_day ): #ไว้เว้นที่เริ่มวันแรก
    print("  ", end=" ")
for day in range(1, m[mm - 1] + 1):
    print(f"{day:<2}", end=" ")
    if (first_day + day) % 7 == 0:
        print()
print()
print('='*20)



# โค้ดเดิม
# m = [31,28,31,30,31,30,31,31,30,31,30,31]

# def what_day_month (dd,mm) :
#     n = 0
#     sumday = 0
#     for i in m :
#         if n == mm-1 :
#             break
#         n = n+1
#         sumday = sumday + i
#     sumday = sumday + dd
   
#     first_day_month = (sumday - 1)%7
#     return(first_day_month)

# mm = int(input('Enter Month : '))

# first_day = what_day_month(1,mm)

# print("----------------------------")
# print(" Su  Mo  Tu  We  Th  Fr  Sa")
# print("----------------------------")
# for i in range(first_day ): #ไว้เว้นที่เริ่มวันแรก
#     print("   ", end=" ")
  
# for day in range(1, m[mm - 1] + 1):
#     print(f" {day:>2}", end=" ")
#     if (first_day + day) % 7 == 0:
#         print()