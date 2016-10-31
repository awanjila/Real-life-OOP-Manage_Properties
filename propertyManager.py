class Property(object):
	def __init__(self, name, type_property, value, status):
		self.name=name
		self.type_property=type_property
		self.value=value
		self.status=status
	def get_property(self):
		return self.name

	def buy_property(self):
		
	def sell_property(self):
 		pass
	def rent_property(self, amount):
		if isinstance(Property, land):
			self.value+=amount
		elif isinstance(Property, house) or isinstance(Property, car):
			self.value=self.value+(12*amount)
		return self.value				
    def add_property(self):
		pass

	def __str__(self):
		return "%s is a %s" % (self.name, self.type_property, self.number, self.value)
house=Property()
land=Property()
car=Property