import time
'''def generator():
    for i in range(10000000):
        yield i
gen=generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
t=time.time()
for i in gen:
    if i==100:
        break
    else:
        print(i,end=' ')
print(time.time()-t)'''
# generator are the methods which do not store all the data at once but it generates the value on the fly :
# It does not store all the value at once to save the memory .
def function():
    for i in range(100000000):
        print(i,end=' ')
t=time.time()
func=function()
print(time.time()-t)
