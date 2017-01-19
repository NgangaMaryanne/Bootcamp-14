class BinarySearch(list):
  def __init__(self, a, b):
    self.a = a
    self.b = b
    lst = [x for x in range (b, a+1, b)]
    self.length = len(lst)
    
  def search(self,x):
    mylist = self.lst
    first = 0
    last = self.length -1
    mydict = {}
    count =0
    while first<last:
      count = count+1
      if first == last:
        return -1
      middle =(first+last)//2
      middle_item = mylist[middle]
      if middle_item == x:
        mydict ['count'] = count
        mydict ['index'] = middle
        return mydict
      else:  
        if middle_item < x:
          first = middle + 1
        else:
          last = middle 
        
        


        
      
