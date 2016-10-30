class Property(object):
	def __init__(self):
		self.name=name;
		self.size=size;
		self.number=number
		self.value=value
	def buy_property(self):

		pass
	def sell_property(self):
		pass
	def rent_property(self):
		pass

	def __str__(self):
    	return "%s is a %s" % (self.name, self.size, self.number, self.value)
class House(Property):
class Land(Property):
class Car(Property):

