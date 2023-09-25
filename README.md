### README for Python Class and Object Instances Example

#### Description:
This Python script demonstrates the creation and utilization of a class and its instances. The class `NewObjectInstance` has an attribute `x`, a constructor method `__init__`, a method `NewMethod`, and a destructor method `__del__`.

#### Class Structure:
- `NewObjectInstance`:
  - `x`: A class attribute initialized to 0.
  - `__init__(self, name)`: Constructor method that initializes the `name` attribute of an instance and prints a message indicating the construction of the object.
  - `NewMethod(self)`: A method that increments the `x` attribute by 1 each time it is called and prints the number of times it has been used.
  - `__del__(self)`: Destructor method that prints a message indicating the destruction of the object.

#### How to Run:
```sh
python script_name.py
```

#### Example Script:
```python
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
```

#### Expected Output:
```
Object instance 1 was constructed.
Object instance 2 was constructed.
Object Method was used 1 times.
Object Method was used 2 times.
Object Method was used 1 times.
Object Method was used 2 times.
```

#### Note:
- The `__del__` method will be called when the object is about to be destroyed, which is typically when the program ends, but the exact timing depends on the Python interpreter's garbage collection mechanism.
- The `x` attribute is shared among all instances of the class unless it is overridden within an instance.

#### Summary:
This README provides the necessary information to understand and run the provided Python script, demonstrating the basic concepts of class, object instances, constructor, methods, and destructor in Python programming.
