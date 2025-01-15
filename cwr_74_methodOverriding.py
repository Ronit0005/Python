class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    #def area(self):
    #    return 3.14*self.radius*self.radius
obj=circle(5)
print(obj.area())
# in inheritance , when there is two methods of same object , and we call those method , then the method from the parent class is called 