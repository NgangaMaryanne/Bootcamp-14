def gen_prime(n):
  prime_numbers=[]
  if isinstance(n,int):
    if n>1:
      for num in range(2, n+1):
        for i in range (2, num):
    	    if (num%i==0):
    				break
        else:
        	prime_numbers.append(num)
      return prime_numbers
    else:
      raise ValueError("Please input a positive integer")
  else:
    raise TypeError("Please input an integer")

      
