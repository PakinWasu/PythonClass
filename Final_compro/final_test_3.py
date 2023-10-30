#user_string = input('Enter Yourstring')
user_string = 'TheWorldIsNotEnough'
result = ''
result = result + user_string[0]
for i in range(1,len(user_string)):
    ch  = user_string[i]  
    if ch.isupper():
        ch = ch.lower()
        result = result + ' '
    result = result + ch
print(result)