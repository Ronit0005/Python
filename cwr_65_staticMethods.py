'''class emplyee:
  def __init__(self,value):
    self.value=value
  @staticmethod
  def show(x):
    print(f'The name of the employee is {x}')
a=emplyee('Rahul')
a.show(20)
b=emplyee('Rounak')
emplyee.show(100)
b.show(200)'''
class employee:
    def __init__(self,name,id,salary):
      self.name=name
      self.id=id
      self.salary=salary
    def show(self):
      print(f"The name of the employee is {self.name} and its id is {self.id} and the salary of the employee is {self.salary}")
    @staticmethod
    def increment(x):
      return int(0.2*x)
a=employee('Rahul',10012,200000)
a.show()
print(f'The increment given to employee number {a.id} name  : {a.name} is ',a.increment(a.salary)) 