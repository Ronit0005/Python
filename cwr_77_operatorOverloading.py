class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'
    def __add__(x,y):
        return vector(x.i+y.i,x.j+y.j,x.k+y.k)
v1=vector(1,2,3)
v2=vector(4,5,6)
print(v1)
print(v2)
print('The sum is : ',v1+v2)