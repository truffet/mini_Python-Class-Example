### README for Python Class Inheritance Example

#### Description:
This modified Python script illustrates class inheritance, where `ChildClass` inherits from `ParentClass`. Instances of both classes are created, and their methods are invoked to demonstrate the inheritance and interaction of attributes and behaviors. The script also includes destruction messages that may be printed when the objects are destroyed, typically when the program exits or when the objects are collected by the garbage collector.

#### Class Structure:
- `ParentClass` (Parent Class):
  - `x`: Class attribute initialized to 0.
  - `origin`: Class attribute initialized to "Parent Class".
  - `__init__(self, name)`: Constructor method initializing the `name` attribute of an instance and printing a construction message.
  - `ParentMethod(self)`: Method incrementing the `x` attribute by 1 each time it is called and printing the number of times it has been used.
  - `__del__(self)`: Destructor method printing a destruction message.

- `ChildClass` (Child Class):
  - Inherits from `ParentClass`.
  - `y`: Class attribute initialized to 0, specific to the child class.
  - `__init__(self, name)`: Constructor method initializing the `name` attribute of an instance and printing a construction message, including the origin of inheritance.
  - `ChildMethod(self)`: Method specific to the child class, incrementing the `y` attribute by 1 each time it is called and printing the number of times it has been used.

#### How to Run:
```sh
python script_name.py
```

#### Example Script:
```python
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
```

#### Expected Output:
```
Object instance 1 was constructed.
Object instance 2 was constructed.
Object instance 3 was constructed and inherited from Parent Class.
Object Method from parent class was used 1 times.
Object Method from parent class was used 2 times.
Object Method from parent class was used 1 times.
Object Method from parent class was used 2 times.
Object Method from parent class was used 1 times.
Object Method from child class was used 1 times.
Object instance 1 was destructed.  # The order and occurrence of destruction messages may vary
Object instance 2 was destructed.  # and are not guaranteed due to Python's garbage collection mechanism.
Object instance 3 was destructed.
```

#### Summary:
This README provides the necessary information to understand and run the modified Python script, demonstrating class inheritance, object instantiation, method invocation, and object destruction in Python programming. The script exemplifies how a child class can inherit attributes and behaviors from a parent class, have its own additional attributes and behaviors, and how instances of these classes interact with their methods. The destruction messages illustrate the potential object lifecycle events in Python, with the caveat that their occurrence and order are not strictly guaranteed.
