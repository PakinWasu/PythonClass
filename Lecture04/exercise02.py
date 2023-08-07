st = input("Enter a string: ")
print('This is What I found about that string:')

if st.isalnum():
    print('The string is alphanumeric.')

if st.isnumeric():
    print('he string contains only digits.')
if st.isalpha():
    print('The string contains only alphabetic characters.')
if st.isspace():
    print('The string contains only whitespace characters.')

if st.islower():
    print('The letters in string are all lowercase.')
if st.isupper():
    print('The letters in string are all uppercase.')
if st.istitle():
    print('The letters in string are all titlecase.')

