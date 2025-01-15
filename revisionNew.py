"""print("Hello world This is a new world created by me")
print("Hii friends This is a new world")"""
'''a=1
b=2
print(a,b,sep="*",end='_')'''
'''a=1
b=2.2
c='Ronit kumar singh'
d=None
print(type(a))
print(type(b))
print(type(c))
print(type(d))'''
#Built in data type in python
''' 1. int
2. float
3. string 
4. none type 
5. boolean 
6. list 
7. tuple 
8. dictionary
'''
#  we can also create a complex data type in python 
'''x=complex(11,11)
print(x)
print(type(x))'''
#bool=True 
#print(bool)
#x=[1,2,3,4,5,6,7,8,9] #list are mutable and its a orderd collection of a data type 
#print(x)
'''y=(1,2,3,4,5,6,7,8,9) # list are immutable and its a orderd collection of a data type 
print(y)
dict={1:'ronit',2:'Rahul',3:'Ritik'}
print(dict)'''
'''a=15
b=7
print('The sum is :',(a+b))
print('The difference is :',(a-b))
print('The product is :',(a*b))
print('the quotient is :',(a/b))
print('the power of a to b is :',(a**b))
print("the floor division :",(a//b))'''
'''a=1.25
b=5.25
print(int(a)+int(b))
'''
'''x=2.3
y=5
print(x+y)'''
#x=input()
#print('The entered value by user is :',x)
'''x=input("Enter the first number :")
y=input('Enter the second number :')
print(x+y)
print(int(x)+int(y))'''
'''print("""Hello world 
This is a new world 
you are welcomed 
this is a multiline string in python which is created my opening closing bracket""")'''
'''name='Ronit'
print(name[0])
print(name[1])
print(name[2])'''
'''name='Ronit'
for i in name:
    print(i,end=' ')'''
# we can get the length of the string by using the len() function 
'''name='ronit123456789'
print('The length of the string is',len(name))'''
# Indexing through an string
'''name='Ronit'
print(name[1:3])
print(name[-4:-1])'''
# There are many function which can be performed on the string but strings are immutable in python
#name='Ronit Kumar Singh'
#print("The original string is :",name)
#print(name.upper())
#print(name.lower())
#print(name.strip())
#print(name.replace('n','h'))
#print(name.split('.'))
#print(name.capitalize())
#print(name.center(100))
#print(name.count('r'))
#print(name.endswith('r',5,11))
#print(name.find('r'))
#print(name.isalnum())
#print(name.isalpha())
#print(name.islower())
#print(name.isupper())
#print(name.isprintable())
#print(name.isspace())
#print(name.title())
#print(name.istitle())
#print(name.swapcase())
# Conditional statements in python 
'''a=int(input("Enter the number to know whether its a positive , negative or a zero "))
if a>0:
    print("a is a positive number")
elif a<0:
    print("a is a negative number")
else:
    print("a is a zero ")'''
#import time 
#time=time.strftime('%H_%M_%S')
#print(time)
'''import time
time=time.strftime('%H')
print(time)
if time==1:
    print("Time is true")
else:
    print("time is not true")'''
'''x=int(input("Enter the variable"))
match x:
    case 1:
        print("The number is one")
    case 2:
        print("The number is Two")
    case _ if x==10:
        print("The enterd number is Ten")
    case _ :
        print("The number is not one or two")'''
'''name='RONIT'
for i in name:
    print(i,end=' ')'''
'''list=['ronit','rahul','rishi','ritik']
for i in list:
    print(i,end=' ')
'''
'''for i in range(11,0,-1):
    print(i,end=' ')'''
'''i=1
while i<11:
    print(i,end=' ')
    i+=1'''
'''i=0
while i<3:
    if i==3:
        break
    else:
        print(i,end=' ')

    i+=1
else:
    print("else block is executed ")'''
'''for i in range(12):
    if i==11:
        break
    elif i==0:
        continue
    else:
        print(f'5 X {i} = {5*i}')'''
'''i=0
while True:
    print(i,end=' ')
    if i>100:
        break
    i+=1'''
# Function is a set of code that performs a specific task whenever it is called 
"""There are two types of function 
1. Built in fuctions : These function are defined and pre coded in python 
eg ., min(),max(),len(),sum(),type(),etc
2. User defined functions : These functions are defined by the user to perform a specific task whenever it is called
"""
'''print(min(1,2,3,4,5))
print(max(1,2,3,4,5,6,7,8,9))
print(len('Ronit'))
print(sum([1,2,3]))
print(type('Ronit'))'''
'''def min(a,b):
    pass'''
'''def maximum(x,y):
    if x>y:
        print("The first number is greater")
    else:
        print("The second number is greater")
maximum()
def minimum():
    print("The minimum number is 10")
minimum()'''
'''def maximum(x=5,y=8):
    if x>y:
        print("first number is greater than second")
    else:
        print("the second number is greater than the first number")
maximum(y=10)'''
'''def tuple(*tup):
    for i in tup:
        print(i,end='\t')
tuple('ronit','rahul','ritik','rishi')'''
'''def dictionary(**dict):
    print(dict)
dictionary({1:'ronit',2:'rahul',3:'ritik'})'''
'''list=[1,2,3,4,5,6,7,8,9]
print(list[0])
print(list[1])
print(list[2])
print(list[3])'''
'''list=[1,2,3,4,5]
if 5 in list:
    print("Item is present in list")
else:
    print("Item is not present in the list")'''
'''name='Ronit Kumar Singh'
if 'nit' in name:
    print("Item is present in the string")
else:
    print("Item is not present in the string")'''
'''list=[1,2,3,4,5,6,7,8,9,0]
print(list[:7:2])'''
'''list=[i*i for i in range(1,11) if i%2==0]
print(list)'''
# List methods in python
#list=[1,1,2,3,4,5,6,7,8,9]
#list.sort(reverse=True)
#print(list.index(5))
#print(list.count(1))
'''mist=list
mist[0]=100'''
'''mist=list.copy()
mist[0]=100'''
#list.insert(1,'New')
#list.append(100)
#list.pop()
#mist=[100,101,102,103]
#list.extend(mist)
#list.pop(2)
#mist=[101,102,103,104]
#kist=list+mist
#print(kist)
'''tuple=(1,2,3,4)
if 5 in tuple:
    print("The number is present in the tuple")
else:
    print("The number is not present in the tuple")'''
'''tuple=(1,2,3,4)
print(tuple[0:3])'''
#print(len(list))
tuple=(1,2,3,4,5)
#print(tuple.index(4))
#print(tuple.count(1))
#print(len(tuple))
'''country='India'
name='Ronit Kumar Singh'
print(f'My name is {name} and I am from {country}')'''
'''price=49.999999999999
print(f'This item is only for {price:.2f}')'''
#print(f'My name is {{name}} and I am from {{country}}')
'''def maximum(x,y):
    #The function takes two number as a input from the user and returns the maximum between them
    if x>y:
        print("First number is greater")
    else:
        print("Second number is greater")
    print(maximum.__doc__)
maximum(10,20)'''
#import this
# pep 8 is a doctument which helps the programmer to know more about python program
# Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
'''a=int(input("Enter the number whose factorial is to be known"))
x=factorial(a)
print(f'The factorial of the number {a} is {x}')'''
# Sets are mutable but they contain different data types of element and we cannot do indexing in sets
#ronny=set()
#print(type(ronny))
# We can search an element in set
'''set={1,2,3,4,'Ronit'}
if 7 in set:
    print("The number is present in the set")
else:
    print("The number is not present in the set")
'''
# we can access the elements of an set using the for loop
'''set={1,2,3,'ronit'}
for i in set:
    print(i,end='\t')'''
s1={1,2,3,4,5,12,13,14}
s2={1,2,12,13,14}
#print(s1.union(s2))
#s1.update(s2)
#print(s1)
#print(s1.intersection(s2))
#s1.intersection_update(s2)
#print(s1)
#print(s1.symmetric_difference(s2))
#s1.symmetric_difference_update(s2)
#print(s1)
#print(s1.difference(s2))
#s1.difference_update(s2)
#print(s1)
#print(s1.isdisjoint(s2))
#print(s1.issuperset(s2))
#print(s2.issubset(s1))
#s1.add('Ronit Kumar Singh')
#s1.remove('Ronit Kumar Singh')
#print('The s1 set is',s1)
# remove() raises an error while discard does not raise an error
#s1.discard('Kumar')
#s1.remove('K')
#s1.pop()
#print('The set s1 is',s1)
#print(s1.pop())
#s1.clear()
#print(s1)
# Though dictionary is an ordered collection of data items but we cannot do indexing in the dictionary
'''list=[1,2,34]
print(list)'''
dict={1:'Ronit',2:'Rishi',3:'Ritik'}
#print(dict[2])
#print(dict.get(3)) 
#print(dict)
#print(dict.keys())
'''for i in dict.values():
    print(i,end='\t')'''
'''for i in dict.keys():
    print(dict[i])
'''
'''for i in dict.items():
    print(i,end='-----')'''
'''for key,value in dict.items():
    print(f'The value to the key {key} is {value}')'''
'''dict.update({4:'Ronny'})
print(dict)'''
#dict.clear()
#print(dict)
'''dict.popitem()
print(dict)
dict.pop(1)'''
'''del dict[2]
print(dict)'''
'''try:
    x=int(input('Enter your age in numbers'))
except Exception as e:
    print(e)
    print("Sorry an error occured")
'''
# Exception Handling in python 
'''try:
    x=int(input("Enter your age in numbers"))
except Exception as E:
    print(E)
    print("Opps an , error occured !")'''
# We can also design an custom error to throw an error !
'''x=int(input("Enter your age in numbers : "))
if x>120 or x<0:
    raise ValueError("The age cannot be greater than 120 or less than 0 ")'''
# Finally Keyword in python 
'''try:
    x=int(input("Enter the age in numbers which cannot be negative or greater than 120 : "))
except :
    print("Age cannot be greater than 120 or less than 0")
finally:
    print("Closing all the files.......")'''
'''import random
x=random.choice([1,2,3,4,5])
print("The randomly generated number is ",x)'''
'''import string
x=string.ascii_letters
print('The alphabets are ',x)'''
'''import random
import string
x=random.choice(string.ascii_letters)
print("The randomly generated alphabets are :",x)'''
'''import random
x=random.choice([1,2,3,4,5])'''
#a=5
#b=10
#c=15 if a>b else 5
#print('The c is :',c)
#print('A') if a>b else print('B')
'''marks=[1,2,3,4,5]
for index,mark in enumerate(marks):
    print(f'The marks at the index {index} is {mark}')'''
'''marks=[1,2,3,4,5]
for index,mark in enumerate(marks,start=1):
    print(f'The marks at the index {index} is {mark}')'''
# global keyword in python 
'''x=4
def function():
    global x
    x=10
    print("The value of x in function is ",x)
function()
print('The value of x in global is ',x)
# The keyword defined in function is different from that which are defined within global'''
# keeping global keyword in function activates the global identity in function
# Reading a file in python programming
'''a=open('ronitFile.txt','r')
x=a.read()
print(x)
a.close()'''
# Writing a file in python 
'''a=open('ronitFile.txt','w')
a.write('Hii I am Ronit kumar singh and i am going to become a successful tech businessman ')
a.close()
'''
# Appending a file in python
'''a=open('ronitFile.txt','a')
a.write("I will retain my semen till 30 years")
a.close()'''
# Using with keyword in python we does not want to close the file 
'''with open('ronitFile.txt','a') as a:
    a.write('I am Ronit Kumar Singh and i am going to shape the future of ai')'''
'''a=open('ronitFile.txt','r')
while True:
    line=a.readline()
    if not line:
        break
    print(line)
a.close()'''
# Reading multiple line in file
'''with open('ronitFile.txt','r') as a:
    while True:
        x=a.readline()
        if not x:
            break
        print(x)'''
# writting multiples lines in file 
'''a=open('ronitFile.txt','w')
note=['I am ronit kumar singh\n','I am going to become a successful tech business\n','I will shape the future of ai and machine learning in the upcoming modern era']
a.writelines(note)
a.close()'''
# by using the seek() method we can changa the cantrol and by using the tell() method we can know whether on which line our cantrol is 
'''with open('ronitFile.txt','w') as a:
   a.seek(3)
   print(a.tell())'''
'''with open('ronitFile.txt','w') as x:
    x.write("hii I am ronit kumar singh and I am india !")
    x.truncate(10)
'''
# lambda expression can be helpful to reduce the function to one line 
'''def square(n):
    return n*n
'''
'''square=lambda x:x*x
print(square(10))'''
# we can also pass a function as a argument to the another function 
'''square=lambda x:x*x
def sum(value,function):
    return value+function(value)
print(sum(10,square))'''
# we can use map method to replace the elements in a list with its square, cube or can do a operation on it
'''kist=[1,2,3,4,5,6]
square=lambda x:x*x
newList=list(map(lambda x:x*x,kist))
print("The list after sunstituing the elements of the list is :",newList)'''
# we can filter the list with the help of filter() method :
'''mist=[1,2,3,4,5,6,7,8,9]
newList=list(filter(lambda x:x>5,mist))
print(newList)'''
# We can reduce a list by reduce() method
'''from functools import reduce
mist=[1,2,3,4,5]
newList=reduce(lambda x,y:x+y,mist)
print(newList)'''
# 'is' vs '==' in python 
# 'is' compares the memory location while '==' compares the value of the variabls 
'''a=5
b=5
print(a==b)
print(a is b)
'''
'''tup1=(1,2,3)
tup2=(1,2,3)
print(tup1==tup2)
print(tup1 is tup2)'''
'''list1=[1,2,3]
list2=[1,2,3]
print(list1==list2)
print(list1 is list2)'''
# Opps concepts in python 
'''class people:
    name='Ronit Kumar Singh'
    occupation='Businessman'
    def profile(self):
        print(f'My name is {self.name} and I am a {self.occupation}')
ronit=people()
ronit.profile()
rahul=people()
rahul.name='Rahul Shah'
rahul.occupation='Software Engineer'
rahul.profile()'''
# Constructors in python 
'''class people:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    def profile(self):
        print(f'My name is {self.name} and I am a {self.occupation}')
ronit=people('Ronit','Businessman')
rahul=people('Rahul','Software Engineer')
ronit.profile()
rahul.profile()'''
'''def greeting(fx):
    def mfx():
        print("Hii")
        fx()
        print('Bye')
    return mfx
@greeting
def profile():
        print('I am Ronit Kumar Singh and I am going to shape the future of modern AI')
profile()'''
# Decorators in python 
'''def greeting(fx):
    def mfx():
        print("START")
        fx()
        print('END')
    return mfx
@greeting
def welcome():
    print("You are welcomed to our event !!!!!")
welcome()'''
'''def greeting(fx):
    def mfx(*x,**y):
        print("START")
        fx(*x,**y)
        print('END')
    return mfx
@greeting
def sum(a,b):
    sum=a+b
    print(f'The sum is {sum}')
q=int(input("Enter the first number : "))
w=int(input("Enter the second number : "))
sum(q,w)'''
'''class people:
    def __init__(self,value):
        self.value=value
    @property
    def profile(self):
        print(f'The price is only {self.value}')
colgate=people(70.00)
colgate.profile'''
'''class emplyoee:
    def __init__(self,value):
        self.value=value
    @property
    def show(self):
        return f'The price is only {self.value}'
    @show.setter
    def setvalue(self,newValue):
        self.value=newValue
    @property
    def test(self):
        return f'The test price is {self.value}'
ronit=emplyoee(45.00)
ronit.setvalue=39.00
print(ronit.show)
print(ronit.test)'''
# Inheritance in python 
'''class parent:
    @property
    def pront(self):
        print("I am a function from a parent class !!!!")
    @property
    def front(self):
        print("I am another function from parent class !!!!!")
class child(parent):
    @property
    def gront(self):
        print("I am a function from a child class !!!")
obj=child()
obj.gront
obj.front
obj.pront
'''
# Access modifiers in python 
# There is no concept of public , private or protected
# private access modifier in python 
'''class people:
    def __init__(self,value):
        self.__value=value
    def profile(self):
        print(f'The price is {self.__value}')
ronit=people('Ronit')
print(ronit._people__value)'''
# protected access modifiers
'''class people:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f'The price of this product is only {self._value}')
ronit=people('Ronit Kumar singh')
print(ronit._value)'''
# static methods in python 
# static method do not take self as a argument
'''class people:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def show(x,y):
        return f'The sum is {sum([x,y])}'
ronit=people('Ronit kumar singh')
print(ronit.show(10,20))'''
'''class people:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def staticFunction(name,occupation):
        print(f'My name is {name} and I am a {occupation}')
ronit=people('Ronit')
ronit.staticFunction('Ronit','Businessman')'''
