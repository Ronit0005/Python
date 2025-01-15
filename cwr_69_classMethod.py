class employee:
    name="rahul kumar shah"
    def show(self):
        print(f'The name of the employee is : {self.name}')
    @classmethod
    def quot(cls,newName):
        cls.name=newName
x=employee()
x.name='Ronit Kumar Singh'
x.show()
x.quot('Ritik Singh')
print(employee.name)