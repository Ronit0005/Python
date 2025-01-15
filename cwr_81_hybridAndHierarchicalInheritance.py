# Hybrid Inheritance : consist of multiple type of inheritance 
# Hierarchical Inheritance : when two child class inherits from a single parent class 
class parent:
    def showDetails(self):
        print("I am a parent class ")
class child1(parent):
    def show(self):
        print("I am a child 1 class")
class child2(parent):
    def show(self):
        print("I am a child 2 class ")
obj1=child1()
obj1.showDetails()
obj2=child2()
obj2.showDetails()