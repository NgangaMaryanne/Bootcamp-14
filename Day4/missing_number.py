def find_missing(lst_a, lst_b):
  a = set(lst_a).union(set(lst_b))
  b = set(lst_a).intersection(set(lst_b))
  #gives a list
  result = list(a-b)
  #display just the number in the list
  
  if result == []:
    return 0
  else:
    for num in result:
      return num
  
  

