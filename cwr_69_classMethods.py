# class methods are the methods which are defined within a class and are associated with the class not the instance 
# on giving a class method decorator in the place of instance or object class name is passed
class employee:

    companyName='Nvidia'
    def showDetails(self):
        print(f'The name is {self.name} and company is {employee.companyName}')
    @classmethod
    def changeCompanyName(cls,newCompanyName):
        cls.companyName=newCompanyName
employee1=employee()
employee1.name='Ronit'
employee1.showDetails()
employee2=employee()
employee2.name='Harry'
employee2.changeCompanyName('Google')
employee2.showDetails()