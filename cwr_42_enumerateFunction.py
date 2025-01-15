index=0 
marks=[12,24,36,48,60,72,84,96,108,120]
for i in marks:
    print(f"The Marks at {index} is {i}")
    index+=1
for index,mark in enumerate(marks,start=8):
    print(f"the marks at index {index} is {mark}")
