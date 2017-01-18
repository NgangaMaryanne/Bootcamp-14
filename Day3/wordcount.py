def words(sentence):
  myword_list = sentence.split()
  newlist=[]
  mywords={}
  for word in myword_list:
    if word.isdigit():
      word = int(word)
      newlist.append(word)
    else:
      newlist.append(word)
  
  for word in newlist:
    if word in mywords:
      mywords[word]=mywords[word]+1
    else:
      mywords[word]=1
  return  mywords
        