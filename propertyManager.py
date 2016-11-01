class Property(object):
	def __init__(self, name, type_property, value, status):
		self.name=name
		self.type_property=type_property
		self.value=value
		self.status=status
	def get_property(self):
		return self.name + self.type_property

	def buy_property(self, amount):
		self.value+=amount
		self.status="bought"
		
	def sell_property(self):
		self.value-=value;
 		self.status="sold"
	def rent_property(self, amount):
		if isinstance(Property, land):
			self.value+=amount
		elif isinstance(Property, house) or isinstance(Property, car):
			self.value=self.value+(12*amount)
		return self.value				
    def add_property(self):
		

	def __str__(self):
		return "%s is a %s whose number is %s and has a value of %s" % (self.name, self.type_property, self.number, self.value)
class House(Property):
	pass
class Land(Property):
	pass
class Car(Property):
	pass