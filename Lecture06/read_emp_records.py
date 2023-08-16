def main():
    data_emp = open('employees.txt', 'r')
    index_name = 1
    index_id = 2
    index_dep = 3

    for indexline,line in enumerate(data_emp,start=1):
        #print(indexline,line)
        line = line.rstrip('\n')
        if indexline == 1 or index_name == indexline:
            index_name = index_name + 3
            name = line
        if indexline == 2 or index_id == indexline:
            index_id = index_id + 3
            id = line
        if indexline == 3 or index_dep == indexline:
            index_dep = index_dep + 3
            dep = line

        if indexline%3 == 0:
            print("Name:",name)
            print('ID:',id)
            print('Dept:',dep)
            
            
    data_emp.close()

main()