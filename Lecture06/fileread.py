def main():
    infile = open('philosophers.txt','r')
    file_contens = infile.read()
    infile.close()

    print(file_contens)

main()