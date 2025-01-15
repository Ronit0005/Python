'''class people:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f'The value of the input is ->',self.value)
    @property
    def get(self):
        return 10 * self.value
ronit=people(10)
ronit.value=100
ronit.show()'''
#If you wants to call a function but not as a function , the prperty decorator is used
'''class people:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @property
    def show(self):
        return f'{self.fname} {self.lname}'
    @show.setter
    def show(self,a):
       self.fname='Ronit Kumar'
ronit=people('Ronit','Singh')'''
#print(ronit.show)
#print(ronit.fname)
#ronit.show
#ronit.fname='Ronit Kumar'
#print(ronit.fname)
#ronit.show='Kumar'
#print(ronit.show)
'''class people:
    def __init__(self,value):
          self.value=value
    def show(self):
        print(f'The value given to the {self.value}')
    @property
    def ten_show(self):
        return 10*self.value
    @ten_show.setter
    def ten_show(self,newvalue):
        self.value=newvalue
ronit=people(25)
ronit.ten_show=24
print(ronit.ten_show)'''
