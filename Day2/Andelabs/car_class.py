
class Car (object):
  
  def __init__( self, name='General', model = 'GM', car_type= None, speed = 0):
    self.name=name
    self.model = model
    self.speed = speed
    self.car_type = car_type
    
    if self.name == 'Porshe' or self.name=='Koenigsegg':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
      
    if self.car_type =='trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
      
  def is_saloon(self):
    if self.car_type != 'trailer':
      self.car_type == 'saloon'
      return True
    else:
      return False

  def drive (self,moving_speed):
    if self.car_type =='trailer':
      self.speed = 77
      
    if self.name=='Mercedes':
      self.speed = 10**moving_speed
    
    return self
    
 