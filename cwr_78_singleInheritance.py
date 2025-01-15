class animal:
    def __init__(self,name,height):
        self.nameOfAnimal=name
        self.heightOfAnimal=height
    def makeSound(self):
        print('Produces an sound........')
'''class dog(animal):
    def __init__(self,name):
        self.name=name
    def makeSound(self):
        print('bark..........')
ob=dog('dog')
ob.makeSound()'''
class cat(animal):
    def __init__(self):
        print("Cat...")
    def makeSound(self):
        print("mew.......")
ob=cat()
ob.makeSound()