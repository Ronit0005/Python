'''x=4
print('the global variable',x)
def ronit():
    x=100
    print('the local variable ',x)
ronit()
print('the global variable',x)
#print(ronit.x)
#print("Hello World ")
'''
x=1
print(f"The global x is {x}")
def fun():
    global x
    x=10
    #print(x)
    #y=1000
    #print(y)

fun()
print(f'The global x is {x}')