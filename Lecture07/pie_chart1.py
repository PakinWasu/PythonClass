import matplotlib.pyplot as plt

def main():
    sales = [100, 400, 300, 600]
    sliceLabels = ['1st Qtr','2nd Qtr', '3rt Qtr', '4th Qtr']
    
    plt.pie(sales, labels=sliceLabels)

    plt.title('Sales by Quarter')
    plt.show()

main()