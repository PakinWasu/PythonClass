def main():
    numDays = int(input('For many day do ' + \
                        'you have sales? '))
    sales_file = open('sales.txt', 'w')


    for count in range(1, numDays + 1):
        sales = float(input('Enter the sales for day #' +
                            str(count) + ': '))
    
        sales_file.write(str(sales) + '\n')
    sales_file.close()
    print('Data written  to sales.txt.')

main()