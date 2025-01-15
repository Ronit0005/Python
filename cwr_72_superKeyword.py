'''class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class programmer(employee):
    def __init__(self,name,salary,id):
        super().__init__(name,salary)
        self.id=id
ronit=programmer('Ronit',1000,'ron001')
print(ronit.name)
print(ronit.salary)
print(ronit.id)'''
class Parent:
    def parentMethod(self):
        print('I am a method from parent class')
class child(Parent):
    def parentMethod(self):
      print("I am a method from child class ")
    def childMethod(self):
        print('I am a method from child class')
       # super().parentMethod()
obj=child()
obj.childMethod()
obj.parentMethod()