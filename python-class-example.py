# parent class
class NewObjectInstance:
	x = 0

	def __init__(self, name):
		self.name = name
		print(f"Object {self.name} was constructed.")

	def NewMethod(self):
		self.x = self.x + 1
		print(f"Object Method from parent class was used {self.x} times.")

	def __del__(self):
		print(f"Object {self.name} was destructed.")

# child class
class NewObjectInheritedInstance(NewObjectInstance):
	y = 0

	def NewMethod2(self):
		self.y = self.y + 1
		print(f"Object Method from child class was used {self.y} times.")

instance1 = NewObjectInstance("instance 1")
instance2 = NewObjectInstance("instance 2")
instance3 = NewObjectInheritedInstance("instance 3")
instance1.NewMethod()
instance1.NewMethod()
instance2.NewMethod()
instance2.NewMethod()
instance3.NewMethod()
instance3.NewMethod2()
