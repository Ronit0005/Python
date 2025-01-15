"""
try:
    a=int(input('enter the value of a'))
    b=int(input('enter the value of ab'))
    print(a/b)
except:
    print("The denominator cannot be zero")
finally:
    print("I am always executed")
"""
"""
def errorThrower():
    try:
      a=int(input('enter the value of a :'))
      b=int(input('enter the value of b :'))
      #print(a/b)
      return a/b
    except:
      print("The denominator cannot be zero")
      return 0
    finally:
      print("I am always executed")
print(errorThrower())
"""
