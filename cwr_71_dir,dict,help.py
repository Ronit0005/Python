#x=[1,2,3,4,5]
#print(dir(x))
#x=(1,2,3,4,5)
#print(dir(x))
'''class employee:
    def __init__(self,x,y):
        self.name=x
        self.salary=y
#print(dir(employee))
Employee=employee('Ronit',12000)
print(Employee.__dict__)
'''
class people:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def showDetails(self):
        print(f'The name of the employee is {self.name} and salary is {self.salary}')
    def front(self):
        print('Hii , This is ronit ')
print(help(people))