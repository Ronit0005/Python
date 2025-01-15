class employee:
    def __init__(self,name):
        self.name=name
    def test(self):
        print(f'The name of the employee is {self.name}')
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def test(self):
        print(f'The name of the dance the employee know is {self.dance}')
class dancerEmployee(dancer,employee):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance
obj=dancerEmployee('Ronit','hip hop')
obj.test()