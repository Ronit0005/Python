'''class people:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def showDetails(self):
        print(f'The name of the employee is {self.name} and his salary is {self.salary}')
obj=people('Ronit',12)
obj.showDetails()'''
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(self,x):
        return self(string.split('_')[0],string.split('_')[1])
    def showDetails(self):
        print(f'The name of the employee is {self.name} and salary is {self.salary}')
string='Ronit_1000'
obj=employee.fromstr(string)
obj.showDetails()