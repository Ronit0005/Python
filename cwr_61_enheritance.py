'''class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #@property
    def showData(self):
        return (f'The age of the person {self.name} is {self.age}')
class child(parent):
      def showen(self):
           print("Hii the default language for coding is python")
#ronit=parent('Ronit',19)
#print(ronit.showData)
rahul=child('Rahul',19)
print(rahul.showData())
rahul.showen()'''
"""class parentClass:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def showDetail(self):
        print(f'The salary of the employ {self.name} id -> {self.id} is {self.salary}')
class childClass(parentClass):
    def performance(self):
        print("The emplyee\'s performance is good ")
#rahul=parentClass('Rahul',10023,'Rs 10 lakhs')
#rahul.showDetail()
aditya=childClass('Aditya',10056,'Rs 10 lakhs')
aditya.showDetail()
aditya.performance()"""