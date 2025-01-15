class Company:
    companyName='Nvidia'
    def __init__(self,name):
        self.name=name
    def showDetail(self):
        print(f"The name of the employee is {self.name} , works at {self.companyName}")
ronit=Company('Ronit')
#Company.companyName='Microsoft'
ronit.name='Rahul'
ronit.companyName='Google'
ronit.showDetail()
rahul=Company('Rahul')
#Company.showDetail(ronit)
rahul.name='Ronit'
rahul.showDetail()
#print(rahul.companyName)