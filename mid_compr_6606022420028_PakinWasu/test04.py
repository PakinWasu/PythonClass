def del_text(text):
    text_list = []
    #print(text)
    for texts in text:
        if texts.isalpha() == False:
            text.remove(texts)
            continue
        #print(texts)
    for text_sort in text:
        text_list.append(text_sort.capitalize())
    #print(text_list) 
    text_list.sort(key=len)
    text_list.reverse()
    return(text_list) 
    
        

print(del_text(['apple','3Banana','Cherry','d4ragonfruit','elderberry']))
print(del_text(['123','Hello','world','Python','99Programming']))
print(del_text(['Ai','65Machine','Learnning','Deep','Learnning101']))