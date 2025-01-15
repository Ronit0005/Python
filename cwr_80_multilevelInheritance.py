class animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def showDetails(self):
        print(f'Name : {self.name}')
        print(f'Type : {self.type}')
class dog(animal):
    def __init__(self,name,type,specie):
        super().__init__(name,type)
        self.specie=specie
    def showDetails(self):
        super().showDetails()
        print(f'Specie : {self.specie}')
class GoldenRetriver(dog):
    def __init__(self,name,type,specie,color):
        super().__init__(name,type,specie)
        self.color=color
    def showDetails(self):
        super().showDetails()
        print(f'Color : {self.color}')
ob=GoldenRetriver('Tommy','Dog','Golden Retriver','Golden white')
ob.showDetails()