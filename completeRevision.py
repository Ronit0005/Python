# pip is a package manager which can be used to install exernal module in python 
#print('Hii this a python world ',' Will you join me in this wonderful journey'
# ,sep='.',end='.')
# variables are like container
# creating a variable means creating a place holder in the memory and assigning
#  it some value 
'''a=1
b=True
c='Ronit'
d=None
e=complex(11,11)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''
#a=55.77
#print(type(a))                                                                                                                                                                                                                                                                                                                                                         
# what is list : List is a ordered collection collection of data separated by 
#                commas and enclosed within square bracket and are mutable 
#list=[1,2,3,45,6,7,8,9]
#print(list)
'''what is tuple : Tuple is a ordered collection of data seprated by comma and 
enclosed with paranthesis , its a non mutable '''
#tuple=(1,2,3,4,5,6,7,8,9)
#print(tuple)
'''what is dictionary : Dictionary is a mapped data which is orderd and mtable
and seprated by comma and enclosed within curly braces'''
#dict={'ronit':'Rajput','rahul':'sahu','aditya':'bumiyar'}
# python has many type of operator for different operation 
'''a=15
b=7
print(f'The sum is {a+b}')
print(f'The difference is {a-b}')
print(f'The product is {a*b}')
print(f'The division is {a/b}')
print(f'The power is {a**b}')
print(f'The floor division is {a//b}')
print(f'The modulus is {a%b}')'''
# Type Casting : The conversion of one data type into another data type 
#There are two types of type casting : Implicit and explict type casting
#  Implicit Type Casting 
'''a=2
b=5.5
c=a+b
print(type(c))'''
# Explicit Type Casting 
'''a=5.65
a=int(a)
print(type(a))'''
'''a='2'
b='5'
print(int(a)+int(b))'''
# We can take user input in python by using input() function 
#userInput=input("Enter a number between 0 and 100")
'''a=input('Enter the first number :')
b=input("Enter the second number :")
print(int(a)+int(b))'''
#x='''Hii I am Ronit Kumar Singh
#What is your name '''
#print(x)
'''name='Ronit Kumar Singh'
for i in name:
    if i=='h':
        print(i)
        break
    print(i,end='_')'''
'''name='Ronit Kumar Singh'
print(name[0])
print(name[1])
print(name[2])'''
# We can calculate the length of a given string by len() function .
'''name='Ronit Kumar Singh'
print(f'The length of the string is {len(name)}')'''
# Indexing through an string 
#name='Ronit Kumar Singh'
#print(name[0:5])
#print(name[-10:-1])
# Strings are immutable in python 
#name='Ronit Kumar Singh'
#print(f'The original string is : {name}')
#print(name.upper())
#print(name.lower())
#print(name.strip())
#print(name.replace('Ronit','Rohit'))
#print(name.split())
#print(name.capitalize())
#print(name.center(100))
#print(name.count('Kumar'))
#print(name.endswith('h'))
#print(name.endswith('r',0,12))
#print(name.find('Kumar'))
#print(name.isalnum())
#print(name.isalpha())
#print(name.islower())
#print(name.isupper())
#print(name.isprintable())
#print(name.isspace())
#print(name.title())
#print(name.capitalize())
#print(name.swapcase())
#print(name.istitle())
   

# Strings are immutable in python 
# Space in python is called Indentation 
# Conditional Statement 
'''a=int(input('Enter the number to know whether It\'s a positive , neagtive or zero '))
if a>0:
    print(f'The number entered is positive ')
elif a<0:
    print("The number is negative ")
else:
    print("The number is zero")'''
#import time 
#time=time.strftime('%H-%M-%S')
#print(f'The time is {time}')
#print(time.time())
#print(time.perf_counter())
'''x=int(input('Enter your age in numbers'))
match x:
    case 1:
        print(f'Your age is {x}')
    case _ if x<=18:
         print(f'Your age is {x} and you are not eligible for driving')
    case _ :
        print(f'Your age is {x}')
'''
# Loops in python is used to execute a grp of statement for certain number of times
# for loop 
'''name='Ronit Kumar Singh'
for i in name:
    print(i,end=' ')'''
# There can also be iteration over a list
'''list=[1,2,3,4,5,6,7,8,9]
for _ in list:
    print("Ronit Kumar Singh")'''
'''for i in range(1,11):
    print(f'5 X {i} = {5*i}')'''
#for i in range(1,100,5):
#    print(i,end=' ')
'''i=1
while i<11:
    print(f'5 X {i} = {5*i}')
    i+=1'''
   


# There is no concept of do while loop in python 
# While loop in python 
'''i=0
while i<5:
    if i==4:
        break
    print(i,end=' ')
    i+=1
else:
    print('Else block is executed successfully')
'''
'''for i in range(1,12):
    if i==11:
        break
    print(f'10 X {i} = {10*i}')
'''
'''for i in range(11):
    if i==0:
        continue
    print(f'2 X {i} = {2*i}')'''
'''i=1
while True:
    print(f'10 X {i} = {10*i}')
    if i==10:
        break
    i+=1'''
# Simulating a do-while loop in Python
'''while True:
    # Code to execute at least once
    num = int(input("Enter a positive number: "))
    
    # Condition check to break the loop
    if num > 0:
        print(f"You entered: {num}")
        break
    else:
        print("Please try again!")
# Simulating a do-while loop in Python
while True:
    # Code to execute at least once
    num = int(input("Enter a positive number: "))
    
    # Condition check to break the loop
    if num > 0:
        print(f"You entered: {num}")
        break
    else:
        print("Please try again!")
# Simulating a do-while loop in Python
while True:
    # Code to execute at least once
    num = int(input("Enter a positive number: "))
    
    # Condition check to break the loop
    if num > 0:
        print(f"You entered: {num}")
        break
    else:
        print("Please try again!")
# Simulating a do-while loop in Python
while True:
    # Code to execute at least once
    num = int(input("Enter a positive number: "))
    
    # Condition check to break the loop
    if num > 0:
        print(f"You entered: {num}")
        break
    else:
        print("Please try again!")
# Simulating a do-while loop in Python
while True:
    # Code to execute at least once
    num = int(input("Enter a positive number: "))
    
    # Condition check to break the loop
    if num > 0:
        print(f"You entered: {num}")
        break
    else:
        print("Please try again!")
'''
# do while loop has a characterstics of executing a block of statement atleast onces
# This can be done using an infinte loop which is-> while True:





# A function is a block of code which performs a specific task whenever it is called 
'''There are two types of function 
    1. Built in function 
     2. User defined function '''
# Some of the Built in functions includes 
'''a=5
b=10
print(min(a,b))
print(max(a,b))'''
'''name='ronit'
print(len(name))'''
#print(sum([1,2,3,4,5,6,7,8,9]))
'''a=1
print(type(a))'''



# user defined functions are defined by the user and can return value
# It is defined by using the keyword def function_name():
'''def maximum(a,b):
    if a>b:
        print(f'The greater number is {a}')
    else:
        print(f'The greater number is {b}')
maximum(10,20)
# A function is not executed by its own   have to call it '''
# This can be done to write a function afterwards
'''def textFunction(x):
    pass 
'''
#   can give a default values to the parameters of a function 
'''def maximum(x=10,y=2):
    if x>y:
        print(f'The greater number is {x}')
    else:
        print(f'The greater number is {y}')
maximum(100)
'''
# If a function is asking for a value and   did't supply , It will throw an error
'''def sum(x,y):
    print(int(x)+int(y))
sum() # Throws an error '''
# We can also give the argument to a function in the form of tuple
'''def tuple(*tup):
    for i in tup:
        print(i,end='\t')
tu=('ronit','kumar','singh','rahul','kumar','shah')
tuple(tu)'''
# We can also give the arguments to a function in the form of dictionary
'''def dictinary(**dict):
    print(dict.keys())
    for key in dict.keys():
        print(f'The value at the key {key} is {dict[key]}')
dictinary(dict={'ronit':101,'Rahul':102,'Amit':103})'''
# List in python :
'''
List is a orderd collection data 
It is mutable(ie.,It can be changed after being created)'''
'''print(marks[0])
print(marks[1])
print(marks[2])'''
# Searching in a list
#marks=[31,34,33,37]
'''if 40 in marks:
    print('Yes It is found !!')
else:
    print('No it didn\'t found')'''
#print(marks[0:2])
#print(marks[:3])
#print(marks[0:])
#list=[i for i in range(10)]
#print(list)
'''list=[i*i for i in range(10)]
print(list)'''
'''list=[i*i*i for i in range(10) if i%2==0]
print(list)'''
#list=[1,2,3,4,5,6,7,8,9]
#print(list.sort(reverse=True))
#list.sort(reverse=True)
#print(list)
#print(list.index(7))
#print(list.count(5))
'''mist=list
mist[0]=100
print(list)'''
'''mist=list.copy()
mist[0]=100
print(list)'''
'''list.insert(1,'Ronit')
print(list)'''
'''list.append(10)
print(list)'''
'''list.pop()
print(list)'''
#list.pop(5)
#print(list)
#mist=[10,11,12,13,14,15]
'''list.extend(mist)
print(list)'''
'''kist=list+mist
print(kist)'''
# Tuples in python 
'''
It's a ordered collection of data 
It is immutable(ie.,it cannot be changed after being created)'''
from typing import Any


tuple=(1,2,3,4,5,6,7,8,9)
#print(tuple.index(5))
#print(tuple.count(5))
#print(len(tuple))
# If you want to add an element to an tuple then first convert the tuple to the list 
# Then perform the operation and then again convert it back to the tuple
#tuple=list(tuple)
#tuple=tuple(tuple)
#print(type(tuple))




# F-strings in python 
'''a=10
b=20
print(f'The value of a is {{a}} and that of b is {{b}}')'''
'''price=35.456274
print(f'The price of the product is {price:.4f}')'''

# Doc strings in python 
#def maximum(x,y):
#    '''Note : This function takes two numbers as a input and prints the greater among them'''
#    print(maximum.__doc__)
#    if x>y:
#        print(f'The greater number is {x}')
#    else:
#        print(f'The greater number is {y}')
#maximum(10,20)
#import this

# Pep stands for python enhancement proposal. 

# Recursion : Recursion is a process of defining something in term of itself. 
'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
'''

# Else for for loop :
'''for i in range(1,12):
    if i==11:
        break   # If cantrol is breaked out of loop , then else block is executed.
    else:
        print(f'10 X {i} = {10*i}')
else:
    print('Else block is execued successfully')'''

# Exception handling 
'''try:
   x=int(input('Enter your age in numbers : '))
except:
   print('OOps an error occured due to some unknown reason')'''
'''age=int(input('Enter your age in numbers : '))
if age>150 or age<0:
    raise ValueError('Enter age between 0 and 150')'''

# There are some condition when   when   have to execute a code even if a exception has occured 
'''def testFunc():
     try:
        x=int(input("Enter a number "))
     except:
         print('OOPs an error has occured due to some unknown reason')
     finally:
         print("Closing all the tabs.....")
testFunc()'''

# Sets in python :
'''Set is unordered collection of data , enclosed within curly braces and seprated 
by comma. 
Set do not contain duplicate item '''
# Printing an empty set :
'''s=set()
print(type(s))'''
# Searching an element in sets:
'''
s={1,2,3,4,5,6,7,8,9}
if 9 in s:
    print('Elemement Found')
else:
    print('Element not found')'''

# Printing the elements of set
'''s={1,2,3,4,5,6}
for i in s:
    print(i,end=' ')'''

# Methods of set :
'''s1={1,2,3,4,5}
s2={1,2,10,11,12}'''
#print(s1.union(s2))
#s1.update(s2)
#print(s1)
#print(s1.intersection(s2))
#s1.intersection_update(s2)
#print(s1)
#print(s1.difference(s2))
#s1.difference_update(s2)
#print(s1)
#print(s1.symmetric_difference(s2))
#s1.symmetric_difference_update(s2)
#print(s1)
#print(s1.isdisjoint(s2))
#print(s1.issuperset(s2))
#print(s1.issubset(s2))
'''s1.add(9)
print(s1)'''
'''s1.remove(1)
print(s1)'''
'''s1.discard(5)
print(s1)'''
# remove raises an error if the elemnent is not found in the set 
# discard does not raises an error if the element is not found in the set 

#print(s1.pop())
'''lis=[1,2,3]
#list.clear()
del lis
print(lis)'''
#del s1
#print(s1)
'''s1.clear()
print(s1)'''
# Dictionary is ordered collection of data , enclosed within curly brackets:
#print(dict)
#print(dict)
'''for i in dict:
    print(i,end=' ')'''
#print(dict['ronit'])  # printing the single element using
#print(dict.keys())

# printing the keys
'''for i in dict.keys():
    print(i,end='\t')'''

# accessing the key and value pairs:
'''for key,value in dict.items():
    print(f'The value at the key {key} is {value}')'''

# for adding elements in the dictionary:
'''dict.update({'rahul':107})
print(dict)'''

'''dict.clear()
print(dict)'''

# removing an element from the dictionary whose key is passed 
'''dict.pop('ronit')
print(dict)'''

# removing random key value paisrs from the dictionary:
#print(dict.popitem())

'''del dict['amit']
print(dict)'''
'''dick={'ronit':101,'amit':103,'rishi':105}
del dick
print(dick)'''


#import random
#import string
#x=random.choice(string.ascii_letters)
#x=string.ascii_letters
#print(x)
#print(type(x))
'''a='abcdey'
x=random.choice(a)
print(x)'''


# Short hands in python:
'''a=2
b=6
c=8 if a>b else 4
print(f'The value of c is {c}')'''
'''age=int(input('Enter your age in numbers :'))
print('You are eligible for license') if age>18 else print("You are not eligible for license ") if age<18 else print("Age is just a number :")
'''

# The enumerate function:
'''tuple=(1,2,3,4,5)
for index,value in enumerate(tuple,start=100):
    print(f'The value at the index {index} is {value}')'''

# Lambda function:
'''def sum(x,y):
    return x+y
print(sum(10,20))
'''
'''square=lambda x,y:x+y
print(square(24,76))'''
# we can also pass function as a argument to another function :
'''def maximum(fx,a):
    return fx(a)
x=maximum(lambda x:x*x ,100)
print(x)'''

# Map:
'''kist=[1,2,3,4,5,6,7,8,9]
newList=list(map(lambda x:x*x*x ,kist))
print(newList)'''

# Filter :
'''l=[1,2,3,4,5,6,7,8,9]
newL=list(filter(lambda x:x>5 ,l))
print(newL)'''

#reduce
'''from functools import reduce
l=[1,2,3,4,5]
newL=reduce(lambda x,y:x*y ,l)
print(newL)'''

# is VS == :
'''is : compares the memory location 
== : compares the value '''
'''a=10
b=10
print(a is b)
print(a == b)'''
'''list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
print(list1 is list2)
print(list2 == list1)'''

# os module 

# Global keyword in a function :
'''print('The value of x before the function ',x:=10)
def overWrite():
    global x
    print('The value of x in the function ',x:=100)
overWrite()
print('The value of x after the function ',x)'''
# writing the global with any variable invokes the global x

# FILE HANDLING IN PYTHON :
# Reading a txt file :
'''x=open('myfile.txt','r')
a=x.read()
print(a)
x.close()'''

# Writing a txt file in python:
'''f=open('myfile.txt','w')
w=f.write('I am hope it is understandable')
print(w)
f.close()'''

# Appending a txt file in python:
'''x=open('myfile.txt','a')
a=x.write(' I am appending this txt file')
x.close()'''

# using with keyword for the file handling , we do not have to close the file 
'''with open('myfile.txt','r') as a:
    print(a.read())'''

# Mutliple line reading in file handling:
'''a=open('myfile.txt','r')
while True:
    line=a.readline()
    if not line:
        break
    print(line)
a.close()'''
'''a=open('myfile.txt','r')
x=(a.readlines())
for i in x:
    l=len(i)
    print(i[:l-1])
a.close()'''

# Multiple line writing :
'''with open('myfile.txt','w') as a:
    write=['Ronit Kumar Singh\n','Hii this is a new world\n','Hope you will like it\n']
    a.writelines(write)
'''

# multiple line writing:
with open('myfile.txt','w') as a:
    a.write('Hiii This a new world\n')
    a.write('Hope you will like it')

# seek and tell:
'''with open('myfile.txt','w') as x:
    x.seek(8)
    print(x.tell())'''

# truncate:
'''with open('myfile.txt','w') as x:
    x.write('My name is Ronit Kumar Singh and what is your name')
    x.truncate(10)
'''

# OPPs in python:
'''class people:
    name='Ronit'
    occupation='Software Engineer'
    def profile(self):
        print(f'The name of the person is {self.name} and his/her occupation is {self.occupation}')
ronit=people()
ronit.profile()
amit=people()
amit.name='Amit'
amit.occupation='Cloud Engineer'
amit.profile()'''

# Constructor:
'''class employee:
    def __init__(self,name):
        self.name=name
    def profile(self):
        print(f'The name of the employee is {self.name}')
ronit=employee('Ronit')
ronit.profile()
amit=employee('Amit')
amit.profile()'''

# Decorator: Is a function which can modify another function:
# when no argument is passed:
'''def greeting(fx):
    def mfx():
        print('Hii')
        fx()
        print('Bye')
    return mfx
@greeting
def profile():
    print('My name is Ronit Kumar Singh And I software engineer')
profile()'''
'''def decorator(fx):
    def mfx(*a,**b):
        print('Hii')
        fx(*a,**b)
        print('Bye')
    return mfx
@decorator
def sum(x,y):
    print(f'The sum is {x+y}')
sum(10,20)'''
# Decorator is used to add somethimg in the front and end of a function:

# Getter: When we want a call a function but not as a function but treat it as a variable:
'''class employee:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    @property
    def profile(self):
        print('Hii')
        return f'The name of the employee is {self.name} and occupation is {self.occupation}'
ronit=employee('Ronit','AI engineer')
print(ronit.profile)
'''
# When we want to call a function but not as function:

# Setter: When we want to give the value to a function directly:
'''class employee:
    def __init__(self,name):
        self.name=name
    @property
    def profile(self):
        return f'The name of the employee is {self.name}'
    @profile.setter
    def changer(self,newValue):
        self.name=newValue
ronit=employee('Ronit')
ronit.changer='King'
print(ronit.profile)'''
# setter can be used to set the values of a variable and it requires another function
# setter can be used with getter only:

# Enheritance:
'''class employee:
    def __init__(self,name):
        self.name=name
    def showDetails(self):
        return f'The name of the employee is {self.name}'
class person(employee):
    def __init__(self,name,occupation):
        super().__init__(name)
        self.occupation=occupation
    @property
    def profile(self):
        return f'The name of the employee is {self.name} and his/her occupation is {self.occupation}'
x=person('Ronit','Businessman')
print(x.profile)'''

# Access modifier:There is no concept of public ,private or protected variable in python:
# private access modifier:
'''class employee:
    def __init__(self,name):
        self.__name=name
    @property
    def profile(self):
        return f'The name of the employee is {self.__name}'
x=employee('Ronit')
x._employee__name='Amit'
print(x.profile)
'''
# variable starting with double underscore is consider as a private variable 
#    It means we cannot access it by normal means we have to use underscore+class name
#        before it for accessing or modifying it .

# protected variable :
'''There is no concept of protected variable in python 
There is just a convension to consider a variable protected if it starts with single underscore'''
'''class employee:
    def __init__(self,name):
        self._name=name
    def profile(self):
        return f'The name of the employee is {self._name}'
emp1=employee('Amit')
print(emp1.profile())'''

'''class employee:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def profile(name):
        return f'The name of the employee is {name}'
x=employee('Ronit')
print(x.profile('Amit'))'''

# class Vs instance variable:
'''class employee:
    companyName='Nvidia'
    def __init__(self,name,comName='Amazon'):
        self.name=name
        employee.companyName=comName
    @property
    def profile(self):
        return f'The name of the employee is {self.name} works at {self.companyName}'
employee.companyName='Nestle'  # to change the global variable of a class:
ronit=employee('Ronit')
ronit.companyName='Google'
print(ronit.profile)
amit=employee('Amit')
print(amit.profile)'''
'''if the instance variable is used in the methods of the class then the system will 
   check for the instance variable but if the instance variable is not found 
   the the class variable is used  '''

# class methods:In these type of methods first parameter is class instance.
'''class employee:
    companyName='Amazon'
    def __init__(self,name):
        self.name=name
    @classmethod
    def classVariableChanger(self):
        print(self)
        self.companyName='Nvidia'
    @property
    def profile(self):
        return f'The name of the employee is {self.name} works at {employee.companyName}'
ronit=employee('Ronit')
ronit.classVariableChanger()
print(ronit.profile)
'''

# Alternative Constructor:class methods can also be used as a construtor 
'''Some times the value to programmer is not supplied as its need 
Hence we define a '''
class employee:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    #@classmethod
    def alternativeConstructor(cls,x):
        return cls(x.split('-')[0],x.split('-')[1]) # This statement calls the constructor of the employee class.
'''x='Ronit-Businessman'
object=employee.alternativeConstructor(x)
print(object.name)
print(object.occupation)'''
#print(employee.alternativeConstructor('Ronit-Businessman'))
#print(employee.alternativeConstructor(object,'Ronit-Businessman'))
# class method can be called without creating an object directly by using the class method

'''Sometimes we are given an unknown class 
And we wants to known something about it 
Then we use dir() , __dict__ , help()'''
'''class employee:
    companyName='Google'
    def __init__(self,name):
        self.name=name
    def profile(self):
        return f'The name of the employee is {self.name} , works at {self.occupation}'
ronit=employee('Ronit')
ronit.companyName='Nvidia'
print(dir(employee))
print(employee.profile)
print(help(employee))
'''
#lst=[1,2,3,4]
#print(dir(lst))
#print(lst.sort)
#print(help(lst))
'''class parent:
    def __init__(self,name):
        self.name=name
    def prof(self):
        return f'The name of the parent is {self.name}'
class child(parent):
    def __init__(self,nameParent,nameChild):
        super().__init__(nameParent)
        self.nameChild=nameChild
    @property
    def profile(self):
        print(super().prof())
        return f'The name of the child is {self.nameChild}'
x=child('Ronit','Sahil')
print(x.profile)'''
# __dict__ method:
'''class employee:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    def profile(self):
        return f'The name of the employee is {self.name} , works at {self.occupation}'
x=employee('Ronit','Businessman')
print(x.__dict__)'''
# this method returns the dictionary which gives which a list of variable assigned to which value

# Super Keyword:
'''class parent:
    def __init__(self,name):
        self.name=name
    def showDetail(self):
        return f'The name of the parent is {self.name}'
class child(parent):
    def __init__(self,name1,name2):
        super().__init__(name1)
        self.name2=name2
    def details(self):
        print(super().showDetail())
        return f'The name of the child is {self.name2}'
x=child('Ronit','Rahul')
print(x.details())
'''

# When there is a same methods in the parent as well as derived class , child class method is preffered over the parent class method
'''class parent:
    def __init__(self):
      print('I am a constructor of parent class')
    def showDetails(self):
        print('I am a method of parent class')
class child(parent):
    def __init__(self):
        print('I am constructor of child class')
    def showDetails(self):
        print('I am a method of child class')
x=child()
x.showDetails()'''

# Dunder or Magic Method :
# 1. __len__
'''class people:
    name='Nvidia'
    def __len__(self):
        return len(self.name)
x=people()
print(len(x))'''

# 2. __call__
'''class people:
    def __call__(self):
        print('I am a dunder __call__ methods')
x=people()
x()'''

# 3. __repr__ or __str__ :They can only return a value they cannot print a value
'''class people:
    def __repr__(self):
        return 'I am a dunder __repr__ method'
    def __str__(self):
        return 'I am a __str__ dunder method'
x=people()
#print(str(x))
#print(str(x))
print(x)''' 
# If only object is printed __str__ method is preferd over __repr__ method.

# Opeator overlaoding in python.
'''class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f'{self.i}i+{self.j}j+{self.k}k'
    def __add__(x,y):
        return vector(x.i+y.i,x.j+y.j,x.k+y.k)
v1=vector(10,20,30)
v2=vector(40,50,60)
print(v1)
print(v2)
print(v1+v2)'''

# Multilevel Inheritance: Level by level inheritance .
'''class grandParent:
    def __init__(self,nameG):
        self.nameG=nameG
    def profile(self):
        return f'The name of the grand parent is {self.nameG}'
class parent(grandParent):
    def __init__(self,nameG,nameP):
        super().__init__(nameG)
        self.nameP=nameP
    def profile(self):
        print(super().profile())
        return f'The name of the parent is {self.nameP}'
class child(parent):
    def __init__(self,nameG,nameP,nameC):
        super().__init__(nameG,nameP)
        self.nameC=nameC
    def profile(self):
        print(super().profile())
        return f'The name of the child is {self.nameC}'
x=child('Satyanaryan Singh','Rabindar Singh','Ronit Kumar Singh')
print(x.profile())'''

# Multiple inheritance: one class inheriting from multiple classes.
'''class father:
    def faceLook(self):
        return f'He looks like his father'
class mother:
    def faceLook(self):
        return f'He looks like his mother'
class child(mother,father):
    pass
x=child()
print(x.faceLook())'''
'''class mother:
    def __init__(self,nameM):
        self.nameM=nameM
    def faceLook(self):
        return f'He looks like her mother'
class father:
    def __init__(self,nameF):
        self.nameF=nameF
    def faceLook(self):
        return f'He looks like his father'
class child(mother,father):
    def __init__(self,nameM,nameF,nameC):
        x=mother(nameM)
        y=father(nameF)
        self.nameC=nameC
x=child('Sarita Devi','Rabindar Singh','Ronit Kumar Singh')
print(x.faceLook())
#print(child.__mro__)'''

# Generating sounds from the speaker using python:
'''import win32com.client
speaker=win32com.client.Dispatch('SAPI.SpVoice')
s='Gandu'
speaker.speak(s)'''

# hierarchial Inheritance:
'''class parent:
    def __init__(self,nameP):
         self.nameP=nameP
    def profile(self):
        return f'The name of the parent is {self.nameP}'
class child1(parent):
    def __init__(self, nameP,nameC):
        super().__init__(nameP)
        self.nameC=nameC
    def profile(self):
        print(super().profile())
        return f'The name of the child is {self.nameC}'
x=child1('Rabindar Singh','Ronit Kumar Singh')
print(x.profile())'''

# shutil module in python :
#import shutil
#shutil.copy('shutilFile1.txt','shutilFile2.txt')
'''This methods copies the content of first file to the second file '''

'''try:
    shutil.copytree('file1.txt','file2.txt')
except:
    print('File not found')
'''
# this method cut the content of first file and paste it to the second and delete the first file.
'''import shutil
shutil.move('a1.txt','a2.txt')'''

# deleting a folder using the shutil module.
'''import shutil
shutil.rmtree('a2.txt')'''

# Generators in python:
'''def generator():
    for i in range(1,100):
        yield i
gen=generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
for i in gen:
    if i==10:
        break
    else:
        print(f'The value generated is {i}')'''
'''import string
def generator():
    for i in string.ascii_letters():
        yield i
gen=generator()
for i in string.ascii_letters:
    if i=='j':
        break
    else:
        print(i,end=' ')'''

# lru cache:are the functions which stores the input and repeats the output if the same output is given another time , without going through the functions.
'''import time
from functools import lru_cache
@lru_cache(maxsize=None)
def complexFunction(x):
    time.sleep(10)
    return f'Answer after final calculation {x*x*x*x*x}'
print(complexFunction(10))
print(complexFunction(19))
print(complexFunction(1))
print(complexFunction(10))
print(complexFunction(19))
'''
'''import time 
from functools import lru_cache
@lru_cache(maxsize=None)
def cgpaCalculator(x,y,z):
    time.sleep(5)
    return (x+y+z)/3.0
print(cgpaCalculator(10,20,30))
print(cgpaCalculator(10,2,30))
print(cgpaCalculator(1,20,30))
print(cgpaCalculator(10,20,30))
print(cgpaCalculator(10,2,30))'''

# AsyncIo:
'''import asyncio
import time
async def study():
    time.sleep(5)
    print(f'Studying....')
async def song():
    time.sleep(5)
    print(f'Sleeping.....') 
async def eat():
    time.sleep(5)
    print(f'eating....')
async def main():
    L=await asyncio.gather(
        eat(),
        song(),
        study()
)
asyncio.run(main())'''

'''import time
import asyncio
async def func1():
    await asyncio.sleep(10)
    print('Func1........')
async def func2():
    await asyncio.sleep(10)
    print('Func2......')
async def func3():
    await asyncio.sleep(10)
    print('Func3........')
async def main():
    L=await asyncio.gather(func1(),func2(),func3())
asyncio.run(main()) '''

'''import asyncio
async def func1():
    await asyncio.sleep(10)
    print('func1.....')
async def func2():
    await asyncio.sleep(10)
    print('func2......')
async def func3():
    await asyncio.sleep(10)
    print('func3.......')
async def main():
    await asyncio.gather(func1(),func2(),func3())
asyncio.run(main())
print('Program terminated successfully......')'''

'''import threading
import time
def complexFunction(s):
    print(f'sleep for {s} seconds')
    time.sleep(s)
    return f'Woke up after {s} seconds'
t1=threading.Thread(target=complexFunction,args=[10])
t2=threading.Thread(target=complexFunction,args=[1])
t3=threading.Thread(target=complexFunction,args=[14])
t4=threading.Thread(target=complexFunction,args=[5])
t5=threading.Thread(target=complexFunction,args=[1])
timeS=time.perf_counter()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t3.join()
#print(t1,t2,t3,t4,t5,sep='-')
print('Time taken for execution is :',(time.perf_counter()-timeS))'''


'''from concurrent.futures import ThreadPoolExecutor
import time
def complexFunction(s):
    print(f'sleeping for {s} seconds')
    time.sleep(s)
    return f'awake after {s} seconds'
def poolTest():
    with ThreadPoolExecutor() as executor:
        f1=executor.submit(complexFunction,10)
        f2=executor.submit(complexFunction,1)
        f3=executor.submit(complexFunction,15)
        f4=executor.submit(complexFunction,2)
        f5=executor.submit(complexFunction,13)
        print(f2.result())
        print(f4.result())
        print(f1.result())
        print(f5.result())
        print(f3.result())
poolTest()'''

# Multiprocessing:

'''import multiprocessing
import time
def complexFunction(s):
    print(f'Sleept for {s} seconds')
    time.sleep(s)
    print(f'woke up after {s} seconds')
if __name__=='__main__':

 p1=multiprocessing.Process(target=complexFunction,args=[10])
 p2=multiprocessing.Process(target=complexFunction,args=[1])
 p3=multiprocessing.Process(target=complexFunction,args=[10])
 p4=multiprocessing.Process(target=complexFunction,args=[5])
 p5=multiprocessing.Process(target=complexFunction,args=[7])
 timeStart=time.perf_counter()
 p1.start()
 p2.start()
 p3.start()
 p4.start()
 p5.start()
 p3.join()
 p1.join()
 print(f'Time taken for execution is :',time.perf_counter()-timeStart)'''
 