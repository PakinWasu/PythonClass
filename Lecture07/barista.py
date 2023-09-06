numEmployees = 6
def main():
    hours = [0] * numEmployees

    for index in range(numEmployees):
        print('Enter the hour worked by employee ', index + 1, ': ' , sep='' ,end='')
        hours[index] = float(input())


    payRate = float(input('Enter the hourly pay rate: '))

    for index in range (numEmployees):
        grossPay = hours[index] * payRate
        print('Gross pat for employee' , index + 1, ': $',format(grossPay, ',.2f'), sep='')
            
            
main()