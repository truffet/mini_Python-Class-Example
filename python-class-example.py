class NewObjectInstance:
	x = 0

	def __init__(self, name):
		self.name = name
		print(f"Object {self.name} was constructed.")

	def NewMethod(self):
		self.x = self.x + 1
		print(f"Object Method was used {self.x} times.")

	def __del__(self):
		print(f"Object {self.name} was destructed.")

instance1 = NewObjectInstance("instance 1")
instance2 = NewObjectInstance("instance 2")
instance1.NewMethod()
instance1.NewMethod()
instance2.NewMethod()
instance2.NewMethod()
