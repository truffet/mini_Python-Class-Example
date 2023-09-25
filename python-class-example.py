# parent class
class ParentClass:
	x = 0
	origin = "Parent Class"

	def __init__(self, name):
		self.name = name
		print(f"Object {self.name} was constructed.")

	def ParentMethod(self):
		self.x = self.x + 1
		print(f"Object Method from parent class was used {self.x} times.")

	def __del__(self):
		print(f"Object {self.name} was destructed.")

# child class
class ChildClass(ParentClass):
	y = 0

	def __init__(self, name):
		self.name = name
		print(f"Object {self.name} was constructed and inherited from {self.origin}.")

	def ChildMethod(self):
		self.y = self.y + 1
		print(f"Object Method from child class was used {self.y} times.")

instance1 = ParentClass("instance 1")
instance2 = ParentClass("instance 2")
instance3 = ChildClass("instance 3")
instance1.ParentMethod()
instance1.ParentMethod()
instance2.ParentMethod()
instance2.ParentMethod()
instance3.ParentMethod()
instance3.ChildMethod()
