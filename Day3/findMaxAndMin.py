def find_max_min(numbers):
  my_max_and_min=[]
  max_num= max(numbers)
  min_num = min(numbers)
  if max_num==min_num:
    my_max_and_min.append(len(numbers))
  else:
    my_max_and_min.append(min_num)
    my_max_and_min.append(max_num)
  return my_max_and_min
  
