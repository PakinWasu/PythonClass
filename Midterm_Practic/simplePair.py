def simplePair(num,re):
  for i in range(1,len(num)+1):
    for j in num:
      if j != i:
        #print(i,j)
        res = i*j
        if res == re:
            return [i,j]
  return "null"
print(simplePair([1,2,3],3))
print(simplePair([1,2,3],6))
print(simplePair([1,2,3],9))