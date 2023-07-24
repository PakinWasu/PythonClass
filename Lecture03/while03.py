import random

print('What is my magic number (1 to 100) ?')
mynumber = random.randint(1,100)
ntrise = 1
yourguess = -1
print(mynumber)

while ntrise <=7 and mynumber != yourguess:
    msg = str(ntrise) + '>>'
    if ntrise == 7 :
        print('last change')

    yourguess =int(input(msg))
    if yourguess > mynumber:
        print('--> too high')
    if yourguess < mynumber:
        print('--> too low')
    ntrise += 1

if yourguess == mynumber:
    print('Yes! it\'s',mynumber)
else:
    print('Sorry! my number is',mynumber)