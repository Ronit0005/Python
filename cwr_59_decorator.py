'''def greeting(fx):
    def mfx(*args,**kwargs):
        print("Good Morning ")
        fx(*args,**kwargs)
        print("Bye bye ")
    return mfx
@greeting
def sum(a,b):
    print("The sum of the two are",a+b)
sum(5,5)
'''
'''def hi_bye(Fx):
    def Mfx():
        print("Hii......")
        Fx()
        print("Bye......")
    return Mfx
@hi_bye
def letter():
    print('Love you ')
letter()'''
'''def operation(fx):
    def mfx(*args,**kwargs):
          print('Opening all the tabs.....')
          print(fx(*args,**kwargs))
          print('Closing all the tabs....')
    return mfx
@operation
def factorial(a):
     fact=1
     for i in range(1,a+1):
        fact=fact*1
     return fact
factorial(100)'''