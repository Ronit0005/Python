from functools import lru_cache
import time
@lru_cache(maxsize=None)
def complicatedFunction(x):
    time.sleep(5)
    return f"The final result is {x}"
print(complicatedFunction(2))
print(complicatedFunction(3))
print(complicatedFunction(9))
print(complicatedFunction(5))
print(complicatedFunction(2))
print(complicatedFunction(5))
print(complicatedFunction(9))