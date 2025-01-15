# public access modifier 
'''class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'The Name of the employee is {self.name} and his age is {self.age}')
ronit=people('Rahul',19)
ronit.name='Rahul Shah'
ronit.show()
'''
# private access modifier
"""class people:
    def __init__(self,name,age):
          self.__name=name
          self.__age=age
    def show(self):
         print(f"The name of the employee {self.__name} and age is {self.__age}")
ronit=people('Rahul Kumar Shah',20)
#print(ronit.__age)
#print(ronit.__name)
print(ronit._people__name)
print(ronit._people__age)"""
# protected access modifiers 
'''class people:
    def __init__(self,name,age):
        self._name=name                   # It is just a rule there is no syntax :
        self._age=age
    def show(self):
        print(f'The name of the employee is {self._name} and the age is {self._age}')
ronit=people('Ronit Kumar Singh',19)
print(ronit._name)'''


