class employee:
    companyName='Apple'
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'The name of the employee is {self.name} works in {self.companyName}')
employee1=employee('Ronit')
employee.companyName='Nestle'
employee1.companyName='Nvidia'
employee1.show()
employee2=employee('Rahul')
employee2.show()