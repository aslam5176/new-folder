#class Emp():
##	def _init_(self, id, name, Add):
##		self.id = id
##		self.name = name
##		self.Add = Add
##
### Class freelancer inherits EMP
##class details(Emp):
##	def _init_(self, id, name, Add, Emails):
##		super()._init_(id, name, Add)
##		self.Emails = Emails
##
##Emp_1 = details(306, "wasim aslam", "python" , "wasimaariz@!.com")
##print('The ID is:', Emp_1.id)
##print('The Name is:', Emp_1.name)
##print('The Address is:', Emp_1.Add)
##print('The gitEmails is:', Emp_1.Emails)
# Python program to demonstrat 
class Animals:

	# Initializing constructor
	def _init_(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals = True

	def isMammal(self):
		if self.mammals:
			print("It is a mammal.")

	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")


class Dogs(Animals):
	def _init_(self):
		super()._init_()

	def isMammal(self):
		super().isMammal()


class Horses(Animals):
	def _init_(self):
		super()._init_()

	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")


# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()
