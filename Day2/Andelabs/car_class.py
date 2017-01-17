class Car (object):
  
  num_of_wheels=None
  num_of_doors = None
  speed = 0

  def __init__(self, *argv):
    self.name= "General"
    self.model = "GM"
    #self.car_type = car_type
    if self.name == 'Porshe' or self.name =='Koenigsegg':
      self.num_of_doors = 2
    else:
      num_of_doors =4
    for arg in argv:
      if arg=='Trailer':
        self.num_of_wheels = 8
      else:
        self.num_of_wheels = 4
      
    
      
      
  def drive(self, gas):
    if gas>0:
      speed = 100
      return gas *speed
    else:
      return Car.speed
    
  def is_saloon(self):
    if self.car_type !='Trailer':
      return 'Saloon'
  
    
