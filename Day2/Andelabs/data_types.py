def data_type(x):
  if isinstance (x, basestring):
    return len(x)
  elif isinstance (x, bool):
    return x
  elif x is None:
    return 'no value'
  elif isinstance (x, int):
    if x<100:
      return 'less than 100'
    elif x==100:
      return 'equal to 100'
    else:
      return 'more than 100'
  elif isinstance (x, list):
    if len(x)<3:
      return None
    else:
      return x[2]
  else:
    return 'program cannot recognise data type given'
