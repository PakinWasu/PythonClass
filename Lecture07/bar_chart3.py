import matplotlib.pyplot as plt

def main():
    leftEdges = [0, 10, 20, 30, 40]

    heights = [100, 200, 300, 400, 500]
    barWidth = 10

    plt.bar(leftEdges,heights,barWidth,color=('g','r','b','y','g'))
    plt.title('Sales by Year')

    plt.xlabel('Year')
    plt.ylabel('Sales')

    plt.xticks([0, 10, 20, 30, 40],
                ['2016','2017','2018','2019','2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
                ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    

    plt.show()

main()