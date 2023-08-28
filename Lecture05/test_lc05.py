st = input('Enter a string : ')
stn = st.lower()
alpha = ''
vowel = 0
con = 0


for j in range(len(stn)):
    char =  stn[j]
    #print(char)
    if char.isalpha() :
        #print(char)
        alpha = alpha + char
#print(alpha)

for k in range(len(alpha)):
    con_char = alpha[k]
    if con_char == 'a' or con_char == 'e' or con_char == 'i' or con_char == 'o' or con_char == 'u':    
        vowel = vowel+1
    else:
        con = con+1

print('Vowel = ', vowel)
print('Consonant = ',con)