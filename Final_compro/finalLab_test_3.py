def cal_words(words):
    scabble = {}
    r = 0
    bestwords = 0
    rest_word = []
    for i in  1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10:
        scabble.update({chr(97+r):i})
        r += 1

    for w in words:
        score = 0
        for ch in w:
            score += scabble[ch]

        print(score)

        if score == bestwords:
            rest_word.append(w)
        elif score > bestwords:
            bestwords = score
            rest_word.clear()
            rest_word.append(w)
        elif score < bestwords:
            pass
    print(rest_word)

cal_words(['got','oh','rents'])