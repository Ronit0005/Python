'''
try :
 x=int(input("Enter the number whose table you want"))
 for i in range(1,11):
    print(f"{x} x {i} = {x*i}")
except:
  print("Exception Occured")
print('Exception crossed')
'''
"""
try :
  a=int(input("Enter Your Age"))
  name="Ronit Kumar Singh"
  print(name[a])
except ValueError :
  print("Invalid Input")
  print("Closing All Tabs")
except IndexError :
  print("Index Out Of Bound Exception")
  """
try:
    age=int(input("Enter Your Age"))
    name='Ronit kumar singh'
    print(name[age])
except ValueError:
    print('Age can be only numbers')
except IndexError:
    print("Array out of bound exception")
