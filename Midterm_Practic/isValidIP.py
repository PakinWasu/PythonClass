def isValidIP(IP):
    IP = IP.split('.')
    print(IP)
    if len(IP)>4 or len(IP)<4:
        print(len(IP))
        return 'false'
    for i in IP:
        ip = int(i)
        if ip > 255 or ip < 0:
            return 'false'
    return 'true'



print(isValidIP('1.2.3.4'))
print(isValidIP('1.2.3'))
print(isValidIP('1.2.3.4.5'))
print(isValidIP('123.45.65.89'))
print(isValidIP('123.456.78.90'))
print(isValidIP('123.045.067.089'))



