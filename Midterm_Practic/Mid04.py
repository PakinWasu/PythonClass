def sore_text(*text):
    text_list = []
    #print(text)
    for t in text:
        #print(t)
        if t.isalpha() == False:
            continue
        t = t.capitalize()
        text_list.append(t)
    text_list.sort(key=len)
    text_list.reverse()
    return(text_list)
   
   

print(sore_text('Hello','pYthon','5Pythonm','world','445'))