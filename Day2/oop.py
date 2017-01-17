class Pet(object):
	no_of_pets = 0
	no_of_legs = 0

	def __init__(self, name, age, sick=False):
		self.name = name
		self.age= age
		self.sick=sick

		Pet.no_of_pets +=1
#class collects data and methods into one object.

#Dog inherits from Pet class
class Dog (Pet):
	no_of_legs = 4
		
	def _isSick(self):
		if self.sick == True:
		  return "Please call the doctor"
		#call veterinary doctor
	def goes_to_walk(self):
		if self.sick is True:
			return "Cannot go to get a walk cause he is sick"
		else:
			return 'when does the dog walker get here'

class Cat (Pet):
	no_of_legs = 4
	def scratches_people(self):
		if self.age<1:
			return "Cat too young and cute to scratch"
		else:
			return "Cat may or may not be dangerous, tread with care"
#cat can go for a walk as long as it is old enough
#here the method is the same as that of the dog class but different functionality
#polymorphism
	def goes_to_walk(self):
		if self.age>3:
			return "Please let the cat out so that it can go for a walk"
		else:
			return "Not old enough yet"
#fish is a pet that inherits from pet class
class Fish(Pet):
	def goes_to_walk(self):
		return "sorry, i can only swim"


daisy = Fish ("DaisyD", 1, False)
Kaity = Cat ("KaityK", 5, True)
Joe = Dog ("joeJ", 7, False)


#sample calling the methods.
print Joe.goes_to_walk()
print Kaity.no_of_legs
print daisy.name
print Pet.no_of_pets

#respective outputs are 
'''
when does the dog walker get here
4
DaisyD
3
'''