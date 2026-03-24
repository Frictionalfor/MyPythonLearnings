class Parent:
    def func1(self):
        print("This function is in parent class")

class Child(Parent):
    def func2(self):
        print("This function is in child class")
object = Child()
object.func1()
object.func2()


class Mother:
    def func1(self):
        print("This function is in Mother class") 
class Father: 
    def func2(self):
        print("This function is in Father class")
class Child(Mother, Father):
    def func3(self):
        print("This function is in Child class")
object = Child()
object.func1()
object.func2()
object.func3()

class Grandfather:
    def func1(self):
        print("This function is in Grandfather class")
class Father(Grandfather):
    def func2(self):
        print("This function is in Father class")
class Child(Father):
    def func3(self):
        print("This function is in Child class")
object = Child()
object.func1()
object.func2()
object.func3()