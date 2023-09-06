def main():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('cities.txt','w')
    
    
    cities = map(lambda x: x+'\n', cities)
    outfile.writelines(cities)
    
    outfile.close()
    
main()