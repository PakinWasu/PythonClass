
keep_going = 'y'


while keep_going == 'y':
    wholesale = float(input('Entre the item\'s wholesale cost: '))
    
    retail_price = wholesale*2.5
    
    print('Retail price: $',\
          format(retail_price, ',.2f'),'.',sep='')
    
    #See if the user want to do another one.
    keep_going = input('Do you have another item?'+ \
                       '(Enter y for yes): ')