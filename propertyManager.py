class Property(object):
	def __init__(self, name, type_property, value, status):
		self.name=name
		self.type_property=type_property
		self.value=value
		self.status=status
	
	def buy_property(self, amount):
		self.value+=amount
		self.status="bought"
		
	def sell_property(self, amount):
		self.value-=amount;
 		self.status="sold"

	def rent_property(self, amount):
		if isinstance(Property, land):
			self.value+=amount
		elif isinstance(Property, House) or isinstance(Property, Car):
			self.value=self.value+(12*amount)
		return self.value				
    def add_property(self):
		

	def __str__(self):
		return "%s is a %s whose number is %s and has a value of %s" % (self.name, self.type_property, self.number, self.value)
class House(Property):
	def calculate_appreciation(self):
		lease_period=99
		intresest_rate=self.value*0.2
		for eachyear in range lease_period:
			self.value+=intresest_rate
			return self.value

	pass
class Land(Property):
	def calculate_appreciation(self):
		lease_period=99
		intresest_rate=self.value*0.75
		for eachyear in range lease_period:
			self.value+=intresest_rate
			return self.value
	pass
class Car(Property):
	def claculate_depreciation(self):
	pass
	def when_to_sell(self):
		pass