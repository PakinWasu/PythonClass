#This program calculaters sales commissions.
#Creare a vaiable to control the loop.
keep_going = 'y'

#Calculate a series of commissions.
while keep_going == 'y':
    #Get a saleperson's sales and commission rate.
    sales = float(input('Entre the amount of sales: '))
    comm_rate = float(input('Entre the commission rate: '))
    
    #Calculate the commission.
    commission = sales*comm_rate
    #Display the commission.
    print('The commission is $',\
          format(commission, ',.2f'),sep='')
    
    #See if the user want to do another one.
    keep_going = input('Do you want to calculate another'+ \
                       'commission (Enter y for yes): ')